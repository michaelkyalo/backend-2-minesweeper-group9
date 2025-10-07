from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, User, Game
from .game_logic import generate_board, reveal_cell

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
game_bp = Blueprint('game', __name__, url_prefix='/game')

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials"}), 401

@game_bp.route('/start', methods=['POST'])
@jwt_required()
def start_game():
    user_id = get_jwt_identity()
    board = generate_board()
    game = Game(user_id=user_id, board_state=board)
    db.session.add(game)
    db.session.commit()
    return jsonify({"message": "Game started", "board": board}), 201

@game_bp.route('/reveal/<int:game_id>/<int:row>/<int:col>', methods=['POST'])
@jwt_required()
def reveal(game_id, row, col):
    user_id = get_jwt_identity()
    game = Game.query.filter_by(id=game_id, user_id=user_id).first()
    if game:
        result = reveal_cell(game.board_state, row, col)
        game.board_state = result['new_board']
        db.session.commit()
        return jsonify(result)
    return jsonify({"message": "Game not found"}), 404
