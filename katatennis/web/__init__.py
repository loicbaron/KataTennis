#!/usr/bin/env python3

import datetime
import zmq

from flask import Flask, jsonify, render_template, request
from katatennis.db.config import config
from katatennis.db.game import Model, Game, GameSchema
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlservice import SQLClient

app = Flask(__name__)

db = SQLClient(config, model_class=Model)

with app.test_request_context():
    db.create_all()

game_schema = GameSchema()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/games/<int:pk>')
def game(pk):
    try:
        game = db.Game.get(pk)
    except IntegrityError:
        return jsonify({"message": "Game could not be found."}), 400
    game_result = game_schema.dump(game)
    print(game_result)
    return render_template('game.html', game=game_result.data)


@app.route('/api/games', methods=['GET'])
def get_games():
    games = db.Game.all()
    # Serialize the queryset
    result = []
    for game in games:
        result.append(game_schema.dump(game))
    return jsonify({'games': result})


@app.route("/api/games/<int:pk>")
def get_game(pk):
    try:
        game = db.Game.get(pk)
    except IntegrityError:
        return jsonify({"message": "Game could not be found."}), 400
    game_result = game_schema.dump(game)
    return jsonify({'game': game_result})


@app.route('/api/games', methods=['POST'])
def post_game():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    # Validate and deserialize input
    try:
        data = game_schema.load(json_data)
        data = data.data
    except ValidationError as err:
        return jsonify(err.messages), 422

    # Create new game
    game = Game(
        playerOne=data['playerOne'],
        playerTwo=data['playerTwo'],
        created=datetime.datetime.utcnow()
    )
    db.save(game)

    result = game_schema.dump(db.Game.get(game.id))

    process_game(result.data)

    return jsonify({"message": "Created new game.",
                    "game": result})


def process_game(game):

    # ZeroMQ Context
    context = zmq.Context()

    # Define the socket using the "Context"
    sock = context.socket(zmq.REQ)
    sock.setsockopt(zmq.LINGER, 0)
    sock.connect("tcp://127.0.0.1:6002")

    # Send a "message" using the socket
    sock.send_json(game)
    message = sock.recv_json()
    print(message)
    # these are not necessary, but still good practice:
    sock.close()
    context.term()
