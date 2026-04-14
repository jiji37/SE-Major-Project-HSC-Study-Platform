from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.get("/api/hello")
def hello():
    return jsonify({"message": "Backend is running!"})


if __name__ == "__main__":
    app.run()
