# main.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import timedelta

app = Flask(__name__)

# CORS: allow development origins (change in production)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Config (use environment variables in production)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    "DATABASE_URL", "postgresql+psycopg2://michael:123456@localhost/minesweeper_db"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "super-secret-key")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class GameRecord(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    rows = db.Column(db.Integer, nullable=False)
    cols = db.Column(db.Integer, nullable=False)
    mines = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String(20), nullable=True)  # "win" / "loss"
    duration = db.Column(db.Integer, nullable=True)   # seconds

# Routes
@app.route("/api/users/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"message": "username and password required"}), 400
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"message": "username taken"}), 409
    hashed = generate_password_hash(data["password"])
    user = User(username=data["username"], password=hashed)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "user created"}), 201

@app.route("/api/users/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"message": "username and password required"}), 400
    user = User.query.filter_by(username=data["username"]).first()
    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"message": "invalid credentials"}), 401
    token = create_access_token(identity=user.id)
    return jsonify({"token": token, "user": {"id": user.id, "username": user.username}}), 200

@app.route("/api/games/new", methods=["POST"])
@jwt_required()
def new_game():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    rows = int(data.get("rows", 10))
    cols = int(data.get("cols", 10))
    mines = int(data.get("mines", 10))
    game = GameRecord(user_id=user_id, rows=rows, cols=cols, mines=mines)
    db.session.add(game)
    db.session.commit()
    return jsonify({"game_id": game.id, "message": "game created"}), 201

@app.route("/api/games/complete", methods=["POST"])
@jwt_required()
def complete_game():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    game_id = data.get("game_id")
    result = data.get("result")
    duration = data.get("duration")
    if not game_id:
        return jsonify({"message": "game_id required"}), 400
    game = GameRecord.query.filter_by(id=game_id, user_id=user_id).first()
    if not game:
        return jsonify({"message": "game not found"}), 404
    game.result = result
    game.duration = duration
    db.session.commit()
    return jsonify({"message": "game updated"}), 200

# health
@app.route("/api/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # create tables if run directly (dev convenience)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
