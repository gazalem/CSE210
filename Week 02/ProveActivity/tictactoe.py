"""
Author: Alan Montoya
Version: 1.0.0
Date: Jan 05th, 2021

Problem Statement:
Create the tic tac toe game
using python

"""

# Plugins or Utils obtain OS utils
import shutil
import os
import random as rd
import re

# Obtain number of column of the shell
terminalSize = shutil.get_terminal_size().columns

# definition how to clear console or terminal screen
# according to the OS
def clear_console():
    """ Clear the console accorging the the OS
    Returns: nothing
    """
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')


# Print title center based on the size of their shell
def title_print(my_tittle):
    """Print a center title in console
    Parameters:
        my_tittle: String of the tittle
    Returns: nothing
    """
    tittle = f'{my_tittle}  - \U0001f601  \n'
    print(tittle.center(terminalSize))

def draw_board(board = [1,2,3,4,5,6,7,8,9], position=1, mark="1"):
    clear_console()
    tittle = 'Tic Tac Toe'
    title_print(tittle)

    board[position-1] = mark.upper()
    # show player board positions
    # to select in the board
    print("Tic Tac Toe Positions")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("\n"*3)

    # show user selection on
    # the game board
    # Actual Game
    print("Tic Tac Toe Game")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n"*3)
    return board


def check_winner(board, player_mark, player_number):
    if board[0] == player_mark and board[1] == player_mark and board[2] == player_mark:
        print(f"{player_number} win!\n")
    elif board[3] == player_mark and board[4] == player_mark and board[5] == player_mark:
        print(f"{player_number} win!\n")
    elif board[6] == player_mark and board[7] == player_mark and board[8] == player_mark:
        print(f"{player_number} win!\n")
    elif board[0] == player_mark and board[3] == player_mark and board[6] == player_mark:
        print(f"{player_number} win!\n")
    elif board[1] == player_mark and board[4] == player_mark and board[7] == player_mark:
        print(f"{player_number} win!\n")
    elif board[2] == player_mark and board[5] == player_mark and board[8] == player_mark:
        print(f"{player_number} win!\n")
    elif board[0] == player_mark and board[4] == player_mark and board[8] == player_mark:
        print(f"{player_number} win!\n")
    elif board[2] == player_mark and board[4] == player_mark and board[6] == player_mark:
        print(f"{player_number} win!\n")
    else:
        print(f"It's a draw!\n")


def player_input():
    user_marker = input("Enter your mark: ")
    user_pattern = "1-9"
    while (user_marker):
        match = re.search(user_pattern, user_marker)
        if match:
            print("great")
            break
        else:
            user_marker = input("Enter your mark: ")
    return user_marker

def players_raffle():
    clear_console()
    tittle = 'Tic Tac Toe'
    title_print(tittle)
    number_to_guess = rd.randint(1, 10)
    found = False
    while not found:
        try:
            guessed = int(input("Please enter a number between 1 and 10 (inclusive): "))
        except ValueError:
            print("You did not enter an integer")
            continue
        if guessed < 0 or guessed > 100:
            print("That is not in the valid range.")
        else:
            if guessed < number_to_guess:
                print(f"{guessed} is too low.")
            elif guessed > number_to_guess:
                print(f'{guessed} is too high.')
            else:
                print(f'{guessed} is the correct number!')
                found = True

def main():
    # board = ["X",2,3,4,"X",6,7,8,"X"]
    # board = draw_board(board, mark="X")
    # check_winner(board, player_mark="X", player_number="Player 2")
    defined = False


if __name__ == "__main__":
    main()