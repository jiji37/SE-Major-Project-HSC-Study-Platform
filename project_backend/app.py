from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import bcrypt
import jwt
import datetime

app = Flask(__name__)
CORS(app)  # allow GitHub Pages to call your API
app.config["SECRET_KEY"] = "yoursecret"

def get_db():
    return sqlite3.connect("database.db")

@app.post("/signup")
def signup():
    data = request.json
    email = data["email"]
    password = data["password"].encode()

    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    db = get_db()
    db.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed))
    db.commit()
    return jsonify({"message": "Signup successful"})

@app.post("/login")
def login():
    data = request.json
    email = data["email"]
    password = data["password"].encode()

    db = get_db()
    user = db.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()

    if user and bcrypt.checkpw(password, user[2]):
        token = jwt.encode(
            {"email": email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)},
            app.config["SECRET_KEY"],
            algorithm="HS256"
        )
        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
