#!/usr/bin/env python3

import logging
import time

from random import random
from sqlservice import SQLClient

from katatennis.db.config import config
from katatennis.db.game import Model, Game
db = SQLClient(config, model_class=Model)

logger = logging.getLogger(__name__)


def run(q):
    """
    Simulate a game between 2 players
    playerOne or playerTwo will randomly score until there is a winner
    """
    print("Worker simulate game starting")

    while True:
        try:
            g = q.get()
            print("worker got the game = {}".format(g))
            game = db.Game.get(g['id'])
            time.sleep(2)
            while not game.has_winner():
                if random() > 0.5:
                    print("playerOne scores")
                    game.player_one_scores()
                    db.Game.save(game)
                    time.sleep(2)
                else:
                    print("playerTwo scores")
                    game.player_two_scores()
                    db.Game.save(game)
                    time.sleep(2)
            print("we got a winner")
            continue
        except Exception as e:
            import traceback
            traceback.print_exc()
            logger.error("Problem with game: {}".format(g))
            continue

    print("Thread end")