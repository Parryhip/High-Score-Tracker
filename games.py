#Nicholas Larsen
import pygame

#Looks for a match in tic-tac-toe
def match(board, letter):
    for row in board:
        matched = True
        for collumn in row:
            if collumn != letter:
                matched = False
        if matched:
            return True
        #uses range to select the correct indexes in the correct rows to find vertical matches
    for collumn in range(3):
        matched = True
        for row in board:
            if row[collumn] != letter:
                matched = False
        if matched:
            return True
    matched = True
    #Uses ranges to select the diagonal squares on the board and checks if they match
    for square in range(3):
        if board[square][square] != letter:
            matched = False
    if matched:
        return True
    matched = True
    for square in range(3):
        if board[square][square - 2] != letter:
            matched = False
    if matched:
        return True
    #Returns false if no matches were found
    return False

def play_again():
    while True:
        answer = input("Would you like to play that game again? y/n:")
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            print('Please enter y or n.')

#Plays the game, tic tac toe.
def tictactoe():
    while True:
        pass
    #CONTINUE HERE
        