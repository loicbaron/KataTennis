#!/usr/bin/env python3
from katatennis.db import db
from katatennis.db.util import must_not_be_blank
from marshmallow import Schema, fields

class Game(db.Model):
    """
    This class instantiates a Tennis Game
    """
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    playerOne = db.Column(db.String(255))
    playerTwo = db.Column(db.String(255))
    scoreOne = db.Column(db.Integer, default=0)
    scoreTwo = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime)

    #def __init__(self, player_one, player_two, score_one=0, score_two=0):
    #
    #    self.playerOne = player_one
    #    self.playerTwo = player_two
    #    self.scoreOne = score_one
    #    self.scoreTwo = score_two

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)

    def __repr__(self):
        return "{}: {} pts VS {}: {} pts".format(self.playerOne, self.scoreOne, self.playerTwo, self.scoreTwo)

    def player_one_scores(self):
        self.scoreOne += 1

    def player_two_scores(self):
        self.scoreTwo += 1

    def get_player_one_score(self):
        return self.translate_score(self.scoreOne)

    def get_player_two_score(self):
        return self.translate_score(self.scoreTwo)

    def translate_score(self, score):
        if score == 0:
            return "love"
        elif score == 1:
            return "fifteen"
        elif score == 2:
            return "thirty"
        elif score == 3:
            return "forty"
        else:
            raise Exception("Illegal score: {}".format(score))

    def is_deuce(self):
        return self.scoreOne >= 3 and self.scoreOne == self.scoreTwo

    def player_with_highest_score(self):
        if self.scoreOne > self.scoreTwo:
            return self.playerOne
        else:
            return self.playerTwo

    def has_winner(self):
        if self.scoreTwo >= 4 and self.scoreTwo >= self.scoreOne + 2:
            return True
        if self.scoreOne >= 4 and self.scoreOne >= self.scoreTwo + 2:
            return True
        return False

    def has_advantage(self):
        if self.scoreTwo >= 4 and self.scoreTwo == self.scoreOne + 1:
            return True
        if self.scoreOne >= 4 and self.scoreOne == self.scoreTwo + 1:
            return True
        return False

    def get_score(self):
        if self.has_winner():
            return self.player_with_highest_score() + " wins"

        if self.has_advantage():
            return "Advantage " + self.player_with_highest_score()

        if self.is_deuce():
            return "Deuce"

        if self.scoreOne == self.scoreTwo:
            return self.translate_score(self.scoreOne) + " all"

        return self.translate_score(self.scoreOne) + " / " + self.translate_score(self.scoreTwo)


class GameSchema(Schema):
    id = fields.Int(dump_only=True)
    playerOne = fields.Str(validate=must_not_be_blank)
    playerTwo = fields.Str(validate=must_not_be_blank)
    scoreOne = fields.Int()
    scoreTwo = fields.Int()
    created = fields.DateTime(dump_only=True)
    score = fields.Method("format_score", dump_only=True)

    def format_score(self, game):
        return "{}".format(game.get_score())