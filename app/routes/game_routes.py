from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .models import db, User

auth_bp = Blueprint("auth", __name__)

# ===== Signup =====
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Username already exists"}), 422
    user = User(username=data["username"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    access_token = create_access_token(identity=user.id)
    return jsonify({"token": access_token, "user": {"id": user.id, "username": user.username}}), 201

# ===== Login =====
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.check_password(data["password"]):
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token, "user": {"id": user.id, "username": user.username}})
    return jsonify({"error": "Invalid credentials"}), 401
