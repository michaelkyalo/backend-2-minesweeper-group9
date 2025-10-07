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

    # ✅ Root route (add this INSIDE create_app)
    @app.route('/')
    def index():
        return {
            "message": "Welcome to the Minesweeper API!",
            "available_endpoints": [
                "/signup",
                "/login",
                "/api/games/new",
                "/api/games",
                "/api/games/reveal/<game_id>",
                "/api/games/flag/<game_id>"
            ]
        }

    return app  # ✅ Keep this as the last line
