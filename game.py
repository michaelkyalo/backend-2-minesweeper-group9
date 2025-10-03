import random
import json
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cell:
    def __init__(self):  
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_mines = 0

    def to_dict(self):
        return {
            "is_mine": self.is_mine,
            "is_revealed": self.is_revealed,
            "is_flagged": self.is_flagged,
            "adjacent_mines": self.adjacent_mines
        }


class MinesweeperGame:
    def __init__(self, rows=8, cols=8, mines=10):  
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self._place_mines()
        self._calculate_adjacent()

    def _place_mines(self):
        cells = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        for r, c in random.sample(cells, self.mines):
            self.grid[r][c].is_mine = True

    def _calculate_adjacent(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.grid[r][c].is_mine:
                    self.grid[r][c].adjacent_mines = self._count_adjacent_mines(r, c)

    def _count_adjacent_mines(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0),  (1, 1)]
        count = 0
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc].is_mine:
                    count += 1
        return count

    def reveal_cell(self, row, col):
        cell = self.grid[row][col]
        if cell.is_revealed or cell.is_flagged:
            return False
        cell.is_revealed = True
        return not cell.is_mine

    def flag_cell(self, row, col):
        cell = self.grid[row][col]
        if not cell.is_revealed:
            cell.is_flagged = not cell.is_flagged

    def to_json(self):
        return json.dumps([[cell.to_dict() for cell in row] for row in self.grid])


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rows = db.Column(db.Integer, nullable=False)
    cols = db.Column(db.Integer, nullable=False)
    mines = db.Column(db.Integer, nullable=False)
    board_state = db.Column(db.Text, nullable=False)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
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
