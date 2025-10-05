from app.db import db
from datetime import datetime
import json

class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    board_state = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="in_progress")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "board_state": json.loads(self.board_state),
            "created_at": self.created_at,
            "status": self.status
        }


class MinesweeperGame:
    def __init__(self, rows=8, cols=8, mines=10):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = self._generate_board()

    def _generate_board(self):
        """Generate a simple board with random mines"""
        import random
        board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        mine_positions = random.sample(
            [(r, c) for r in range(self.rows) for c in range(self.cols)],
            self.mines
        )
        for r, c in mine_positions:
            board[r][c] = "💣"
        return board

