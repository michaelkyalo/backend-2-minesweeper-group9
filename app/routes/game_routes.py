from flask import Blueprint, request, jsonify
from ..db import db
from ..models.game import Game
from ..services.minesweeper_logic import MinesweeperGame
import json


bp = Blueprint("games", __name__)

@bp.route("/new", methods=["POST"])
def new_game():
    data = request.get_json() or {}

    rows = data.get("rows", 8)
    cols = data.get("cols", 8)
    mines = data.get("mines", 10)

    game = MinesweeperGame(rows, cols, mines)

  
    game_record = Game(
        rows=rows,
        cols=cols,
        mines=mines,
        board_state=json.dumps(game.to_json())
    )
    db.session.add(game_record)
    db.session.commit()

    return jsonify({
        "message": "New game started",
        "game_id": game_record.id,
        "board": game.to_json()
    }), 201


# 🧩 Reveal a cell
@bp.route("/reveal/<int:game_id>", methods=["POST"])
def reveal(game_id):
    game_record = Game.query.get_or_404(game_id)
    data = request.get_json() or {}

    row = data.get("row")
    col = data.get("col")

    if row is None or col is None:
        return jsonify({"error": "Row and column are required"}), 400

    state = json.loads(game_record.board_state)
    game = MinesweeperGame.from_json(state)

    result = game.reveal_cell(row, col)
    game_record.board_state = json.dumps(game.to_json())
    db.session.commit()

    return jsonify({
        "message": "Cell revealed",
        "safe": result,
        "board": game.to_json()
    })


@bp.route("/flag/<int:game_id>", methods=["POST"])
def flag(game_id):
    game_record = Game.query.get_or_404(game_id)
    data = request.get_json() or {}

    row = data.get("row")
    col = data.get("col")

    if row is None or col is None:
        return jsonify({"error": "Row and column are required"}), 400

    state = json.loads(game_record.board_state)
    game = MinesweeperGame.from_json(state)

    game.toggle_flag(row, col)
    game_record.board_state = json.dumps(game.to_json())
    db.session.commit()

    return jsonify({
        "message": "Cell flagged/unflagged",
        "board": game.to_json()
    })



@bp.route("/", methods=["GET"])
def list_games():
    games = Game.query.order_by(Game.created_at.desc()).all()
    return jsonify([
        {"id": g.id, "rows": g.rows, "cols": g.cols, "mines": g.mines}
        for g in games
    ])
