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
    #Checks if all the values in one row of the board are the same
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
        #2-square on a 3 collumn board gives the reverse square, 
        #ie. square 1 becomes sqaure 3, sqaure 2 to square 2, and square 3 to sqaure 1
        if board[square][2 -square] != letter:
            matched = False
    if matched:
        return True
    #Returns false if no matches were found
    return False

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
def tictactoe():
    rowOne = [" ", " ", " "]
    rowTwo = [" ", " ", " "]
    rowThree = [" ", " ", " "]
    board = [rowOne, rowTwo, rowThree]
    while True:
        player = input("Would you like to be X, O or E to leave?\n").upper()
        if player == 'E':
            return False
        elif player != 'X' and player != 'O':
            print("Please enter, X, O, or E.")
        else:
            break
    if player == 'X':
        while True:
            winner = player_turn(board, 'X')
            if winner == 'cat':
                return False
            elif winner == 'player':
                return True
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
                return True
            continue
            
#runs the code to play a number guessing game
def guessing_game():
    import random
    while True:
        guesses = 0
        #Allows the user to choose a range to guess between
        choice = input("What range would you like to guess between?\n1: 1 - 10\n2: 1 - 100\n3: 1 - 1000\n4: Leave\n")
        if choice == '4':
            return False
        #Sets between as a list with the range selected
        elif choice == '1':
            between = [1, 10]
        elif choice == '2':
            between = [1, 100]
        elif choice == '3':
            between = [1, 1000]
        else:
            print("Please enter 1, 2, 3, or 4.")
            continue
        #chooses a number between the selected range
        num = random.randint(between[0], between[1])
        while True:
            guess = input("What number would you like to guess?\n")
            try:
                #checks if you entered a number
                int(guess)
            except:
                print(f"Please enter a number between {between[0]} and {between[1]}.")
                continue
            #checks if you entered a number within the right range
            if int(guess) <= between[1] and int(guess) >= between[0]:
                #decides if your number is too high, too low, or accurate
                if int(guess) > num:
                    print("Too high.")
                    guesses += 1
                elif int(guess) < num:
                    print("Too low.")
                    guesses += 1
                elif int(guess) == num:
                    guesses += 1
                    print(f"You got it in {guesses} tries!")
                    return guesses
            else:
                print(f"Please enter a number between {between[0]} and {between[1]}.")
                continue

#Uses pygame to create a reaction time game
def reaction_times():
    import pygame
    import time
    import random
    #Allows me to use the functions of pygame
    pygame.init()
    #Defines a color for the variables white and black using hex codes
    white = (255, 255, 255)
    black = (0, 0, 0)
    print("After a random period of time, a window will appear. Click when the window appears.")
    
    #Chooses a random time to wait
    wait =  random.randint(1, 10)
    #waits
    time.sleep(wait)
    #Sets window to a display of a certain size
    window = pygame.display.set_mode((400, 400))
    #Sets the name of the window that pops up
    pygame.display.set_caption('Reaction Time Test')
    #Sets a font for pygame to use
    font = pygame.font.SysFont('monospace', 32)
    #Creates an object with text on it that can be displayed
    text = font.render('Click Now!', True, white, black)
    #Creates a rect object to house the text
    text_rect = text.get_rect()
    #Centers the text
    text_rect.center = (200, 200)
    #Starts the timer
    start = time.time()
    while True:
        #Makes the window appear black
        window.fill(black)
        #Makes the text appear on the rectangle
        window.blit(text, text_rect)
        for event in pygame.event.get():
            #Continously loops to check if the user tried to quit, and updates the display afterwards.
            if event.type == pygame.QUIT:
                pygame.quit()
                reaction_time = False
                return reaction_time
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                reaction_time = time.time() - start
                print(f"You reacted in {round(reaction_time, 2)} seconds.")
                return reaction_time
            pygame.display.update()
        
#Main ui to access the games
def game_ui(username):
    from update import update_high_score as update
    choice = input("Which game do you want to play?\n1:Tic Tac Toe\n2:Number Guessing Game\n3:Reaction time game\n4:Exit\n")
    if choice == '1':
        if not tictactoe():
            return
        else:
            update(username, 1)
        #NEED TO FIGURE OUT HOW TO MAKE IT WORK WITH DANIEL'S CODE
    elif choice == '2':
        result = guessing_game()
        if not result:
            return
        else:
            update(username, result)
        #NEED TO FIGURE OUT HOW TO MAKE IT WORK WITH DANIEL'S CODE
    elif choice == '3':
        result = reaction_times()
        if not result:
            return
        else:
            update(username, result)
        #NEED TO FIGURE OUT HOW TO MAKE IT WORK WITH DANIEL'S CODE
    elif choice == '4':
        return
    else:
        print("Please enter 1, 2, 3, or 4.")