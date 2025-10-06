from flask import Flask
from .db import db
from .config import Config
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    from .routes.user_routes import bp as user_bp
    from .routes.game_routes import bp as game_bp

    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(game_bp, url_prefix="/api/games")


    @app.route("/")
    def index():
        return {
            "message": "Welcome to the Minesweeper API!",
            "available_endpoints": [
                "/api/users/register",
                "/api/users/",
                "/api/games/new",
                "/api/games/",
                "/api/games/reveal/<game_id>",
                "/api/games/flag/<game_id>"
            ]
        }

    return app