from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.models import db
from app.auth_routes import auth_bp
from app.game_routes import game_bp
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
CORS(app, supports_credentials=True)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(game_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
