# app/__init__.py
import os
from flask import Flask, send_from_directory
from flask_migrate import Migrate
from flask_cors import CORS

from .models import db
from .routes import auth_bp, game_bp  # we'll create this file

def create_app():
    # If you plan to serve frontend build from backend, static_folder points to frontend/dist
    static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend/dist"))
    app = Flask(__name__, static_folder=static_folder, static_url_path="/")

    app.config.from_object("config.Config")

    # init extensions
    db.init_app(app)
    Migrate(app, db)

    # allow your local dev frontend origins (adjust ports you use)
    CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://localhost:5179"]}})

    # register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(game_bp, url_prefix="/game")

    # Serve the frontend if it's been built to frontend/dist
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def serve_frontend(path):
        if app.static_folder and path != "" and (app.static_folder and (app.static_folder + "/" + path)):
            # if file exists, return it
            try:
                return send_from_directory(app.static_folder, path)
            except Exception:
                pass
        # default to index.html
        if app.static_folder:
            return send_from_directory(app.static_folder, "index.html")
        return {"message": "Minesweeper API running"}

    return app
