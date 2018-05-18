#!/usr/bin/env python3


class Game:
    """
    This class instantiates a Tennis Game
    """

    def __init__(self, player_one, player_two, score_one=0, score_two=0):

        self.playerOne = player_one
        self.playerTwo = player_two
        self.scoreOne = score_one
        self.scoreTwo = score_two

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
