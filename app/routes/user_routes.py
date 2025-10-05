from flask import Blueprint, request, jsonify
from ..db import db
from ..models.user import User

bp = Blueprint("users", __name__)


@bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json() or {}

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")


    if not username or not email or not password:
        return jsonify({"error": "All fields (username, email, password) are required"}), 400

  
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400


    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201



@bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([
        {"id": u.id, "username": u.username, "email": u.email}
        for u in users
    ])
