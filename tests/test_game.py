#!/usr/bin/env python3

from katatennis import Game


game = Game("Mario", "Luigi")


def test_init_game():
    print(game)
    assert hasattr(game, 'playerOne')
    assert hasattr(game, 'playerTwo')


def test_love_all():
    score = game.get_score()
    print(score)
    assert score == "love all"


def test_player_one_scores():
    game.player_one_scores()
    score = game.get_score()
    print(score)
    assert score == "fifteen / love"


def test_fifteen_all():
    game.player_two_scores()
    score = game.get_score()
    print(score)
    assert score == "fifteen all"


def test_set_score():
    new_game = Game("Yoshi", "Toad", 0, 2)
    score = new_game.get_score()
    print(score)
    assert score == "love / thirty"


def test_one_wins():
    new_game = Game("Yoshi", "Toad", 4, 0)
    score = new_game.get_score()
    print(score)
    assert score == "Yoshi wins"


def test_two_wins():
    new_game = Game("Yoshi", "Toad", 1, 4)
    score = new_game.get_score()
    print(score)
    assert score == "Toad wins"


def test_deuce():
    new_game = Game("Yoshi", "Toad", 4, 4)
    score = new_game.get_score()
    print(score)
    assert score == "Deuce"


def test_advantage():
    new_game = Game("Yoshi", "Toad", 5, 4)
    score = new_game.get_score()
    print(score)
    assert score == "Advantage Yoshi"


def test_wins_after_advantage():
    new_game = Game("Yoshi", "Toad", 6, 8)
    score = new_game.get_score()
    print(score)
    assert score == "Toad wins"


def test_simulate_game():
    new_game = Game("Mario", "Luigi", 0, 0)
    score = new_game.get_score()
    print(score)
    assert score == "love all"

    # 15 - 0
    new_game.player_one_scores()
    score = new_game.get_score()
    print(score)
    assert score == "fifteen / love"

    # 30 - 0
    new_game.player_one_scores()
    score = new_game.get_score()
    print(score)
    assert score == "thirty / love"

    # 30 - 15
    new_game.player_two_scores()
    score = new_game.get_score()
    print(score)
    assert score == "thirty / fifteen"

    # 30 - 30
    new_game.player_two_scores()
    score = new_game.get_score()
    print(score)
    assert score == "thirty all"

    # 40 - 30
    new_game.player_one_scores()
    score = new_game.get_score()
    print(score)
    assert score == "forty / thirty"

    # 40 - 40
    new_game.player_two_scores()
    score = new_game.get_score()
    print(score)
    assert score == "Deuce"

    # 40 advantage - 40
    new_game.player_one_scores()
    score = new_game.get_score()
    print(score)
    assert score == "Advantage Mario"

    # 40 - 40
    new_game.player_two_scores()
    score = new_game.get_score()
    print(score)
    assert score == "Deuce"

    # 40 advantage - 40
    new_game.player_one_scores()
    score = new_game.get_score()
    print(score)
    assert score == "Advantage Mario"

    # Mario wins
    new_game.player_one_scores()
    score = new_game.get_score()
    print(score)
    assert score == "Mario wins"
