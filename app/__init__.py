from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from .db import db
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from .routes.game_routes import bp as game_bp
    app.register_blueprint(game_bp, url_prefix="/api/games")

    return app
