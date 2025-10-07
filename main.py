from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# ✅ Allow React frontend at port 5176 to access backend API
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5176"}})

# Database config (update user/password to your actual PostgreSQL credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://user:password@localhost/minesweeper_db'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


# Login route
@app.route("/api/users/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.password == data["password"]:
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token, "message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401


# Protected route example
@app.route("/api/games/new", methods=["POST"])
@jwt_required()
def new_game():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Game created for user {current_user}"}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
