# main.py
from app import create_app  # ✅ Only this

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
