#Nicholas Larsen

#Checks if the board is full
def full(board):
    for row in board:
        for column in row:
            if column == ' ':
                return False
    return True

#Looks for a match in tic-tac-toe
def match(board, letter):
    for row in board:
        matched = True
        for column in row:
            if column != letter:
                matched = False
        if matched:
            return True
        #uses range to select the correct indexes in the correct rows to find vertical matches
    for column in range(3):
        matched = True
        for row in board:
            if row[column] != letter:
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
        if board[square][2 -square] != letter:
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
def check(board, row, column, letter):
    if board[row-1][column-1] == ' ':
        board[row-1][column-1] = letter
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
        column = input("What column would you like to place in? Left is 1, middle is 2, and right is 3.\n")
        if column != '1' and column != '2' and column != '3':
            print("Please enter 1, 2, or 3.")
            continue
        if not check(board, int(row), int(column), letter):
            print("Please don't place on an occupied tile.")
            continue
        if not match(board, letter):
            if full(board):
                view_board(board)
                print("Cat won.")
                return 'cat'
            else:
                return 'none'
        else:
            view_board(board)
            print("You won!")
            return 'player'

#Runs a turn for the computer
def cpu_turn(board, letter):
    import random
    while True:
        row = random.randint(1, 3)
        column = random.randint(1, 3)
        if not check(board, row, column, letter):
            continue
        else:
            if not match(board, letter):
                if full(board):
                    view_board(board)
                    print("Cat won.")
                    return 'cat'
                else:
                    return 'none'
            else:
                view_board(board)
                print("CPU won. :(")
                return 'computer'

        

#Plays the game, tic tac toe.
def tictactoe(username):
    rowOne = [" ", " ", " "]
    rowTwo = [" ", " ", " "]
    rowThree = [" ", " ", " "]
    board = [rowOne, rowTwo, rowThree]
    while True:
        player = input("Would you like to be X, O or E to leave?\n")
        if player.upper() == 'E':
            return False
        elif player.upper() != 'X' and player.upper() != 'O':
            print("Please enter, X, O, or E.")
        else:
            break
    if player == 'X':
        while True:
            winner = player_turn(board, 'X')
            if winner == 'cat':
                return False
            elif winner == 'player':
                return True, username
            winner = cpu_turn(board, 'O')
            if winner == 'cat':
                return False
            elif winner == 'computer':
                return False
            continue
    elif player == 'O':
        while True:
            winner = cpu_turn(board, 'X')
            if winner == 'cat':
                return False
            elif winner == 'computer':
                return False
            winner = player_turn(board, 'O')
            if winner == 'cat':
                return False
            elif winner == 'player':
                return True, username
            continue
            
#runs the code to play a number guessing game
def guessing_game(username):
    import random
    while True:
        guesses = 0
        choice = input("What range would you like to guess between?\n1: 1 - 10\n2: 1 - 100\n3: 1 - 1000\n4: Leave\n")
        if choice == '4':
            return False
        elif choice == '1':
            between = [1, 10]
        elif choice == '2':
            between = [1, 100]
        elif choice == '3':
            between = [1, 1000]
        num = random.randint(between[0], between[1])
        while True:
            guess = input("What number would you like to guess?\n")
            try:
                int(guess)
            except:
                print(f"Please enter a number between {between[0]} and {between[1]}.")
                continue
            if int(guess) <= between[1] and int(guess) >= between[0]:
                if int(guess) > num:
                    print("Too high.")
                    guesses += 1
                elif int(guess) < num:
                    print("Too low.")
                    guesses += 1
                elif int(guess) == num:
                    print(f"You got it in {guesses} tries!")
                    guesses += 1
                    return username, guesses, between
            else:
                print(f"Please enter a number between {between[0]} and {between[1]}.")
                continue

"CREATE REACTION TIME GAME"