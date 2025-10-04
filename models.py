from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rows = db.Column(db.Integer, nullable=False)
    cols = db.Column(db.Integer, nullable=False)
    mines = db.Column(db.Integer, nullable=False)
    board_state = db.Column(db.Text, nullable=False)  # JSON representation
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_active = db.Column(db.Boolean, default=True)

    def serialize(self):
        return {
            "id": self.id,
            "rows": self.rows,
            "cols": self.cols,
            "mines": self.mines,
            "board_state": json.loads(self.board_state),
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat()
        }