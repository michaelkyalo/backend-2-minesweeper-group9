from .db import db
from sqlalchemy.dialects.postgresql import JSONB

class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(JSONB, nullable=False)
    status = db.Column(db.String(20), default="ongoing")

    def serialize(self):
        return {
            "id": self.id,
            "board": self.board,
            "status": self.status,
        }
