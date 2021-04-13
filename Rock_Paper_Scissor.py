# -*- coding: utf-8 -*-

""" Rock Paper Scissor """

__author__ = "Lars Schneckenburger"
__credits__ = "Lars Schneckenburger"
__version__ = "1.0"
__created__ = "10.10.2020"


import random

game_mode = int(input("""Choose game mode:
1 = 1 Player
2 = 2 Player"""))

player_wins = 0
computer_wins = 0
counter_rounds = 0
draw = None
invalid_input = None

while (player_wins < 3 and computer_wins < 3 and game_mode == 2) or (player_wins < 1 and computer_wins < 1 and draw != True  and invalid_input != True and game_mode == 1):
    # Input
    #  Player
    choice_player = input("Scissors, Stone oder Paper?)
    choice_player = choice_player.upper()
    # Computer
    random_number = int(random.uniform(1, 4))
    if random_number == 1:
        choice_computer = "Scissors"
    elif random_number == 2:
        choice_computer = "Stone"
    elif random_number == 3:
        choice_computer = "Paper"
    
    print("Computer:", choice_computer[0] + choice_computer.lower()[1:])
    
    # None
    draw = None
    invalid_input = None

    # processing

    # controll input
    if choice_player not in ["Scissors", "Stone", "Paper"]:
        invalid_input = True
    # player wins
    elif choice_player == "Scissors" and choice_computer == "Paper":
        player_wins += 1
    elif choice_player == "Stone" and choice_computer == "Scissors":
        player_wins += 1
    elif choice_player == "Paper" and choice_computer == "Stone":
        player_wins += 1
    # draw
    elif choice_player == choice_computer:
        draw = True
    # computer wins
    else:
        computer_wins += 1
    # invalid_input
    if invalid_input and game_mode == 2:
        print("Invalid Input!")
    # print
    elif game_mode == 2:
        counter_rounds += 1
        if draw:
            print(f"""Round {counter_rounds} draw""")
        else:
            print(f"""round {counter_rounds}
Spieler: {player_wins}
Computer: {computer_wins}""")


# end
if (player_wins == 3 and game_mode == 2) or (player_wins == 1 and game_mode == 1):
    print("You win!")
elif draw:
    print("Draw")
elif invalid_input:
    print("Invalid input, computer wins!")
else:
    print("Computer wins!")
