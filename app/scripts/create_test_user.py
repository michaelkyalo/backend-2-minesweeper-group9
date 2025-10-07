# scripts/create_test_user.py
from main import db, User, app
from werkzeug.security import generate_password_hash

def create_test_user(username="testuser", password="Testpass123!"):
    with app.app_context():
        if User.query.filter_by(username=username).first():
            print("User already exists")
            return
        u = User(username=username, password=generate_password_hash(password))
        db.session.add(u)
        db.session.commit()
        print("Created", username)

if __name__ == "__main__":
    create_test_user()
