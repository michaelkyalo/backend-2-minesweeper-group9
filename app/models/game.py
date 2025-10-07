from app.db import db

from datetime import datetime
import json

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rows = db.Column(db.Integer, nullable=False)
    cols = db.Column(db.Integer, nullable=False)
    mines = db.Column(db.Integer, nullable=False)
    board = db.Column(db.Text, nullable=False)  # store board as JSON string
    status = db.Column(db.String(20), default='ongoing')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, rows, cols, mines, board):
        self.user_id = user_id
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = json.dumps(board)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "rows": self.rows,
            "cols": self.cols,
            "mines": self.mines,
            "board": json.loads(self.board),
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }