from flask import Blueprint, request, jsonify
from app import db
from app.models import Game, User
import random

bp = Blueprint('games', __name__)


def create_board(rows, cols, mines):
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    mine_positions = set()

    while len(mine_positions) < mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        mine_positions.add((r, c))

    for r, c in mine_positions:
        board[r][c] = 'M'
       
        for i in range(max(0, r - 1), min(rows, r + 2)):
            for j in range(max(0, c - 1), min(cols, c + 2)):
                if board[i][j] != 'M':
                    board[i][j] += 1
    return board



@bp.route('/new', methods=['POST'])
def new_game():
    data = request.get_json()
    user_id = data.get('user_id')
    rows = data.get('rows', 5)
    cols = data.get('cols', 5)
    mines = data.get('mines', 5)

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    board = create_board(rows, cols, mines)
    game = Game(user_id=user.id, rows=rows, cols=cols, mines=mines, board=board)
    db.session.add(game)
    db.session.commit()

    return jsonify({"message": "Game created successfully", "game_id": game.id})


# -----------------------
# Route: Get all games
# -----------------------
@bp.route('/', methods=['GET'])
def get_games():
    games = Game.query.all()
    return jsonify([game.to_dict() for game in games])


# -----------------------
# Route: Reveal a cell
# -----------------------
@bp.route('/reveal/<int:game_id>', methods=['POST'])
def reveal_cell(game_id):
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')

    game = Game.query.get(game_id)
    if not game:
        return jsonify({"error": "Game not found"}), 404

    game.reveal_cell(row, col)  # Implement this in Game model
    db.session.commit()

    return jsonify({
        "message": f"Cell ({row}, {col}) revealed",
        "board": game.board
    })


# -----------------------
# Route: Flag or unflag a cell
# -----------------------
@bp.route('/flag/<int:game_id>', methods=['POST'])
def flag_cell(game_id):
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')

    game = Game.query.get(game_id)
    if not game:
        return jsonify({"error": "Game not found"}), 404

    game.toggle_flag(row, col) 
    db.session.commit()

    return jsonify({
        "message": f"Cell ({row}, {col}) flagged/unflagged",
        "board": game.board
    })
