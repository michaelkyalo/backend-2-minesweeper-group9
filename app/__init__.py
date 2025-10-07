from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from .models import db, User, Game  # ✅ include models
from .routes import auth_bp, game_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    Migrate(app, db)
    CORS(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(game_bp)

    @app.route('/')
    def index():
        return {"message": "Welcome to the Minesweeper API"}

    return app
