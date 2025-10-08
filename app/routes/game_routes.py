from flask import Blueprint, request, jsonify
from ..models import Game
from ..db import db
from ..game_logic import create_board, reveal_cell

bp = Blueprint("games", __name__)

@bp.route("/", methods=["POST"])
def create_game():
    data = request.get_json()
    rows = data.get("rows", 8)
    cols = data.get("cols", 8)
    mines = data.get("mines", 10)

    board = create_board(rows, cols, mines)
    new_game = Game(board=board)
    db.session.add(new_game)
    db.session.commit()

    return jsonify(new_game.serialize()), 201


@bp.route("/<int:game_id>/reveal", methods=["POST"])
def reveal(game_id):
    data = request.get_json()
    row, col = data["row"], data["col"]

    game = Game.query.get_or_404(game_id)
    updated_board, status = reveal_cell(game.board, row, col)
    game.board = updated_board
    game.status = status
    db.session.commit()

    return jsonify(game.serialize()), 200


@bp.route("/", methods=["GET"])
def get_all_games():
    games = Game.query.all()
    return jsonify([g.serialize() for g in games])
