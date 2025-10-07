from flask import Flask
from flask_migrate import Migrate
from .models import db
from .routes import auth_bp, game_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(auth_bp)
    app.register_blueprint(game_bp)

    return app
