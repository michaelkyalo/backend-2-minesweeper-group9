from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS  # ✅ Import CORS
from .models import db
from .routes import auth_bp, game_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # ✅ Initialize extensions
    db.init_app(app)
    Migrate(app, db)

    # ✅ Enable CORS (allow frontend access)
    # You can specify exact ports your React frontend uses (5173, 5176, etc.)
    CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://localhost:5176"]}})

    # ✅ Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(game_bp)

    # ✅ Root route for testing
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

    return app  # ✅ Return app at the end
