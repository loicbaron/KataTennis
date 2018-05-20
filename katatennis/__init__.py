#!/usr/bin/env python3

import os
from flask import Flask, jsonify, render_template, request
from katatennis.db import db
from katatennis.db.game import Game, GameSchema
from marshmallow import ValidationError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db/database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.test_request_context():
    db.create_all()

game_schema = GameSchema()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/games', methods=['GET'])
def get_games():
    games = Game.query.all()
    # Serialize the queryset
    result = game_schema.dump(games)
    return jsonify({'games': result})


@app.route('/api/games', methods=['GET'])
def post_game():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    # Validate and deserialize input
    try:
        data = game_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    # Create new game
    game = Game(
        playerOne=data['playerOne'],
        playerTwo=data['playerTwo'],
        author=author,
        posted_at=datetime.datetime.utcnow()
    )
    db.session.add(game)
    db.session.commit()
    result = game_schema.dump(Game.query.get(game.id))
    return jsonify({"message": "Created new game.",
                    "game": result})
