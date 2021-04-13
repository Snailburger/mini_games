# -*- coding: utf-8 -*-

""" 'Draw a match' game"""

__author__ = "Lars Schneckenburger"
__credits__ = "Lars Schneckenburger"
__version__ = "1.0"
__created__ = "01.03.2021"

"""
The game (simple version) The game starts with a stack of matches
(random number: no less than 10, no more than 20). The players are playing one
after another. A player can either draw one, two or three matches from the
stack per turn. The player who draws the last match loses.
"""

import random

# Function print matches
def print_matches(matches):
    """
    Parameters
    ----------
    matches : Int
        Number of matches which should be print in the Console.

    Returns
    -------
    None.

    """
    if matches > 4:
        for i in range(6):
            if i != 3:
                print("========O")
            else:
                print("...")
    else:
        for i in range(matches):
            print("========O")
    txt = "|The stack has {} matches.|\n"
    print(txt.format(matches))


def computer(matches, mode):
    """
    Parameters
    ----------
    matches : Int
        Number of matches which are still in the game.
    mode : Int
        Game mode which they are playing.

    Returns
    -------
    draw_computer : Int
        Numbers of matches the computer takes.

    """
    if matches == 1:
        draw_computer = 1
    # game mode easy
    elif mode == 2:
        if matches > 2:
            draw_computer = int(random.uniform(1, 4))
        else:
            draw_computer = int(random.uniform(1, 3))
    # game mode hard
    else:
        if matches % 4 == 0:
            draw_computer = 3
        elif matches % 4 == 3:
            draw_computer = 2
        elif matches % 4 == 2:
            draw_computer = 1
        elif matches % 4 == 1:
            draw_computer = int(random.uniform(1, 4))
    txt = "The computer takes {} matches\n"
    print(txt.format(draw_computer))
    return draw_computer


def player(matches):
    """
    Parameters
    ----------
    matches : Int
        Number of matches which are still in the game.

    Returns
    -------
    draw_player : Int
        Numbers of matches a player takes.

    """
    while True:
        options_draw = ["1", "2", "3"]
        print("It's your turn, how many matches do you wanna draw? (1 to 3)")
        draw_player = input()
        if draw_player not in options_draw:
            print("Invalid input. Choose a number between 1 and 3!")
        elif matches < int(draw_player):
            print("You can not take more matches than there are in the game!")
        else:
            break
    return int(draw_player)


# Game
play = True
while play:
    txt = "Author: {}\nCredits: {}\n"
    print(txt.format(__author__, __credits__))
    # Game settings
    # Random number of matches
    number_matches = int(random.uniform(10, 21))
    # Choose game mode
    game_modes = {"1": "Player vs Player", "2": "Player vs Computer (easy)",
                  "3": "Player vs Computer (hard)",
                  "4": "Computer vs Computer"}
    options_modes = ["1", "2", "3", "4"]
    while True:
        print("Choose a game mode")
        for key, value in game_modes.items():
            print(key, ': ', value)
        game_mode = input()
        if game_mode not in options_modes:
            print("Invalid input. Choose a number between 1 and 4!")
        else:
            game_mode = int(game_mode)
            break
    # Random starter
    set_player = int(random.uniform(1, 3))

    # Game
    while number_matches > 0:
        # Print matches
        print_matches(number_matches)
        # Player 1
        if set_player % 2 == 0:
            if game_mode != 4:
                print("Player 1:")
                number_matches -= player(number_matches)
            else:
                print("Computer 1:")
                number_matches -= computer(number_matches, game_mode)

        # Player 2
        else:
            if game_mode == 1:
                print("Player 2:")
                number_matches -= player(number_matches)
            elif game_mode == 4:
                print("Computer 2:")
                number_matches -= computer(number_matches, game_mode)
            else:
                print("Computer:")
                number_matches -= computer(number_matches, game_mode)
        # Player changer
        set_player += 1

    # Winner
    print_matches(number_matches)
    if set_player % 2 == 0:
        if game_mode != 4:
            print("Player 1, you are the winner!")
        else:
            print("Computer 1 is the winner")
    else:
        if game_mode == 1:
            print("Player 2, you are the winner!")
        elif game_mode == 4:
            print("Computer 2 is the winner!")
        else:
            print("Computer is the winner!")

    # Restart
    options_restart = ["YES", "NO"]
    while True:
        restart = input("Do you wanna play one more time? (Yes/No)")
        if restart.upper() not in options_restart:
            print("Invalid Input!")
        else:
            if restart.upper() == "NO":
                play = False
            break
