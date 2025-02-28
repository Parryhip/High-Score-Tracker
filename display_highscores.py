#-------------------------------------------------------------------------------------------Matthew's Code-------------------------------------------------------------------------------------------#

#function to print the tictactoe leaderboard
def print_tictactoe_leaderboard():
    #imports sam's function to take the tictactoe high scores, aliased
    from retrieve_high_scores import retrieve_tic_tac_toe as retrieve 
    #countable variable
    count = 1
    high_scores = retrieve()
    #iterating through high_scores and printing them
    for user in high_scores:
        print(count,".",user, ":",high_scores[user])
        count += 1
        if count > 11:
            break
    else:
        #make it so that when they want to leave, they can just press enter
        input("Enter anything to continue")
        return

#function to print the number guessing leaderboards
def print_numguessing_leaderboard(rangestr):
    #imports sam's funtion to take the number guessing high scores, aliased
    from retrieve_high_scores import retrieve_num_guessing as retrieve 
    #countable variable
    count = 1
    #which of the 3 types of number guessing game variables, or prints one, user presses enter, prints next, user presses enter, prints next
    high_scores = retrieve(rangestr)
    print(f'{rangestr}:')
    #iterating through high_scores and printing them
    for user in high_scores:
        print(count,".",user, ":",high_scores[user])
        count += 1
        if count > 11:
            break
    else:
        #make it so that when they want to leave, they press enter
        input("Enter anything to continue")
        return

#function to print the reaction speed leaderboards
def print_reactionspeed_leaderboard():
    #imports sam's function to take the reactoin speed high scores, aliased
    from retrieve_high_scores import retrieve_reaction_speed as retrieve
    #countable variable
    count = 1
    high_scores = retrieve()
    #iterating through high_scores and printing them
    for user in high_scores:
        print(count,".",user, ":",high_scores[user])
        count += 1
        if count > 11:
            break
    else:
        #make it so that when they want to leave, they can press enter
        input("Enter anything to continue")
        return

#UI function for my part of the code
def choose_leaderboard():
    #infinite loop
    while True:
        #user input to see which one they want to do
        try:
            choice = int(input("What leaderboard would you like to see?\nPress 1 for Tic Tac Toe\nPress 2 for Number Guessing Game\nPress 3 for Reaction Speed Game\nPress 4 to leave leaderboards\n:"))
        #if it's not an integer, it prints not a number
        except:
            print("Not a number!")
            continue
        #calls function to print the tictactoe leaderboard
        if choice == 1:
            print_tictactoe_leaderboard()
        #calls function for each of the numberguessing leaderboards
        elif choice == 2:
            print_numguessing_leaderboard('1-10')
            print_numguessing_leaderboard('1-100')
            print_numguessing_leaderboard('1-1000')
        #calls function to print the reaction speed leaderboard
        elif choice == 3:
            print_reactionspeed_leaderboard()
        #breaks out of this part and goes to the main function
        elif choice == 4:
            return
        #if it's not an integer, it gives this message and makes them try again
        else:
            print("You didn't put in one of the given numbers!")
            continue


#-------------------------------------------------------------------------------------------End of Matthew's Code-------------------------------------------------------------------------------------------#