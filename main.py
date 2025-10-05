from app import create_app
from app.db import db  # ✅ Needed for flask db commands (Migrate to detect models)

app = create_app()

# ✅ Expose `app` and `db` for flask-migrate
# This makes `flask db init`, `flask db migrate`, and `flask db upgrade` work
if __name__ == "__main__":
    app.run(debug=True)
