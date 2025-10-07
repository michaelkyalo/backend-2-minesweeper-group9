from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize database and migration
    db.init_app(app)
    Migrate(app, db)

    # Import and register blueprints
    from .routes import auth_bp, game_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(game_bp)

    return app
