from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  # ✅ explicit table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    games = db.relationship('Game', backref='user', lazy=True)

class Game(db.Model):
    __tablename__ = 'games'  # ✅ explicit table name
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # ✅ must match table name
