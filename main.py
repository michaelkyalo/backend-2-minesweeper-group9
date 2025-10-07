from flask import Flask
from flask_migrate import Migrate
from app import models, routes, database

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minesweeper.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
    models.db.init_app(app)
    app.register_blueprint(routes.bp, url_prefix='/api')
    return app

app = create_app()
migrate = Migrate(app, models.db)

if __name__ == '__main__':
    app.run(debug=True)
