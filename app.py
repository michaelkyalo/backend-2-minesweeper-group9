from flask import Blueprint, request, jsonify
from app import db
from app.models import Game
from app.game import MinesweeperGame

bp = Blueprint("api", _name_)

@bp.route("/new", methods=["POST"])
def new_game():
    data = request.json or {}
    rows = data.get("rows", 8)
    cols = data.get("cols", 8)
    mines = data.get("mines", 10)

    game = MinesweeperGame(rows, cols, mines)
    game_record = Game(
        rows=rows,
        cols=cols,
        mines=mines,
        board_state=game.to_json()
    )
    db.session.add(game_record)
    db.session.commit()

    return jsonify({"message": "New game started", "game": game_record.serialize()})


@bp.route("/reveal/<int:game_id>", methods=["POST"])
def reveal(game_id):
    game_record = Game.query.get_or_404(game_id)
    data = request.json
    row, col = data["row"], data["col"]

    # Load state
    import json
    state = json.loads(game_record.board_state)

    cell = state[row][col]
    if cell["is_revealed"] or cell["is_flagged"]:
        return jsonify({"message": "Cell already revealed/flagged", "game": game_record.serialize()})

    cell["is_revealed"] = True
    safe = not cell["is_mine"]

    game_record.board_state = json.dumps(state)
    db.session.commit()

    return jsonify({"safe": safe, "game": game_record.serialize()})


@bp.route("/flag/<int:game_id>", methods=["POST"])
def flag(game_id):
    game_record = Game.query.get_or_404(game_id)
    data = request.json
    row, col = data["row"], data["col"]

    import json
    state = json.loads(game_record.board_state)

    cell = state[row][col]
    if not cell["is_revealed"]:
        cell["is_flagged"] = not cell["is_flagged"]

    game_record.board_state = json.dumps(state)
    db.session.commit()

    return jsonify({"message": "Cell flagged/unflagged", "game": game_record.serialize()})


@bp.route("/games", methods=["GET"])
def list_games():
    games = Game.query.order_by(Game.created_at.desc()).all()
    return jsonify([g.serialize() for g in games])