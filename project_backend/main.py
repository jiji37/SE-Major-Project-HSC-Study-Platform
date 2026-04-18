from flask import Flask
from flask_restx import Api,Resource,fields
from config import DevConfig
from models import Recipe
from exts import db
from flask_migrate import Migrate


app=Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

migrate=Migrate(app,db)

api=Api(app,doc='/docs')

#model (serializer)
recipe_model=api.model(
    'Recipe',
    {
        'id':fields.Integer(),
        'title':fields.String(),
        'description':fields.String()
    }
)


@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello World"}




@api.route('/recipes')
class RecipesResource(Resource): #unneeded
    @api.marshal_list_with(recipe_model)
    def get(self):
        """Get all recipes"""
        recipes=Recipe.query.all()
        return recipes
    
    @api.expect(recipe_model)
    def post(self):
        """Create a new recipe"""
        data=api.payload
        title=data.get('title')
        description=data.get('description')
        recipe=Recipe(title=title,description=description)
        recipe.save()
        return {"message":"Recipe created successfully"},201



@api.route('/recipe/<int:id>')
class RecipeResource(Resource): #unneeded
    @api.marshal_with(recipe_model)
    def get(self,id):
        """Get a recipe by id"""
        recipe=Recipe.query.get_or_404(id)
        return recipe
    
    @api.expect(recipe_model)
    def put(self,id):
        """Update a recipe by id"""
        recipe=Recipe.query.get_or_404(id)
        data=api.payload
        title=data.get('title')
        description=data.get('description')
        recipe.update(title,description)
        db.session.commit()
        return {"message":"Recipe updated successfully"}
    
    def delete(self,id):
        """Delete a recipe by id"""
        recipe=Recipe.query.get_or_404(id)
        recipe.delete()
        return {"message":"Recipe deleted successfully"}


@app.shell_context_processor
def make_shell_context():
    return{
        "db":db,
        "Recipe":Recipe
    }






if __name__ == '__main__':
    app.run()