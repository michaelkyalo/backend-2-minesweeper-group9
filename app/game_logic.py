import random

def create_board(rows, cols, mines):
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    mine_positions = set()

    while len(mine_positions) < mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        mine_positions.add((r, c))

    for r, c in mine_positions:
        board[r][c] = "M"

        for i in range(max(0, r - 1), min(rows, r + 2)):
            for j in range(max(0, c - 1), min(cols, c + 2)):
                if board[i][j] != "M":
                    board[i][j] += 1

    return board


def reveal_cell(board, row, col):
    if board[row][col] == "M":
        return board, "lost"
    # Simple demo logic — mark as revealed
    board[row][col] = "R"
    return board, "ongoing"
