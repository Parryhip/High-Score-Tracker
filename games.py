#Nicholas Larsen

#Checks if the board is full
def full(board):
    for row in board:
        for collumn in row:
            if collumn == ' ':
                return False
    return True

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

#Prints the board in a way that looks like an actual tic-tac-toe board
def view_board(board):
    for idx, item in enumerate(board):
        for index, i in (enumerate(item)):
            print(i, end = "")
            if index != 2:
                print("|", end = "")
        print("")
        if idx != 2:
            print("-----")

#Checks that the player/CPU isn't trying to place a letter on an occupied square
def check(board, row, collumn, letter):
    if board[row-1][collumn-1] == ' ':
        board[row-1][collumn-1] = letter
        return True
    else:
        return False
    
#Plays one of the player's turns
def player_turn(board, letter):
    while True:
        view_board(board)
        row = input("What row would you like to place in? Top is 1, middle is 2, and bottom is 3.\n")
        if row != '1' and row != '2' and row != '3':
            print("Please enter 1, 2, or 3.")
            continue
        collumn = input("What collumn would you like to place in? Left is 1, middle is 2, and right is 3.\n")
        if collumn != '1' and collumn != '2' and collumn != '3':
            print("Please enter 1, 2, or 3.")
            continue
        if not check(board, row, collumn, letter):
            print("Please don't place on an occupied tile.")
            continue
        if not match(board, letter):
            if full(board):
                print("Cat won")
                return 'cat'
            else:
                return 'none'
        else:
            print("You won!")
            return 'player'

#Runs a turn for the computer
def cpu_turn(board, letter):
    import random
    while True:
        row = random.randint(1, 3)
        collumn = random.randint(1, 3)
        if check(board, row, collumn, letter)
        CONTINUE HERE

#Plays the game, tic tac toe.
def tictactoe():
    while True:
        rowOne = [" ", " ", " "]
        rowTwo = [" ", " ", " "]
        rowThree = [" ", " ", " "]
        board = [rowOne, rowTwo, rowThree]
        while True:
            player = input("Would you like to be X, O or E to leave?")
            if player.upper() == 'E':
                return False
            elif player.upper() != 'X' and player.upper() != 'O':
                print("Please enter, X, O, or E.")
            else:
                break
        if player == 'X':
            winner = player_turn(board, 'X')
            if winner == 'cat':
                return 'cat'
            elif winner == 'player':
                return 'player'
            
            
        else:
            
        


        