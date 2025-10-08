# main.py
from app import create_app  # ✅ Only this import

app = create_app()

if __name__ == "__main__":
    # Debug should be True only in development
    app.run(host="127.0.0.1", port=5000, debug=True)
