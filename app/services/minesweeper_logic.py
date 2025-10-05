import random

class MinesweeperGame:
    def __init__(self, rows=8, cols=8, mines=10):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = self._create_board()
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]

    def _create_board(self):
        board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        mine_positions = random.sample(
            [(r, c) for r in range(self.rows) for c in range(self.cols)],
            self.mines
        )

        for r, c in mine_positions:
            board[r][c] = -1 

          
            for i in range(max(0, r-1), min(self.rows, r+2)):
                for j in range(max(0, c-1), min(self.cols, c+2)):
                    if board[i][j] != -1:
                        board[i][j] += 1

        return board

    def reveal_cell(self, row, col):
        """Reveal a cell; returns result and updates state."""
        if self.revealed[row][col]:
            return {"message": "Already revealed", "board": self.get_board_state()}

        self.revealed[row][col] = True

        if self.board[row][col] == -1:
            return {"message": "Game Over! You hit a mine.", "board": self.board}


        if self.board[row][col] == 0:
            for i in range(max(0, row-1), min(self.rows, row+2)):
                for j in range(max(0, col-1), min(self.cols, col+2)):
                    if not self.revealed[i][j]:
                        self.reveal_cell(i, j)

        return {"message": "Cell revealed", "board": self.get_board_state()}

    def get_board_state(self):
        """Return board state with unrevealed cells hidden."""
        state = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                if self.revealed[r][c]:
                    row.append(self.board[r][c])
                else:
                    row.append(None)
            state.append(row)
        return state
