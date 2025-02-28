#-------------------------------------------------------------------------------------------Matthew's Code-------------------------------------------------------------------------------------------#

def print_tictactoe_leaderboard():
    from retrieve_high_scores import retrieve_tic_tac_toe as retrieve 
    count = 1
    high_scores = retrieve()
    for user in high_scores:
        print(count,".",user, ":",high_scores[user])
        count += 1
        if count > 11:
            break
    else:
        input("Enter anything to continue")
        return
        
        #make it so that when they want to leave, they can just press enter


def print_numguessing_leaderboard(rangestr):
    from retrieve_high_scores import retrieve_num_guessing as retrieve 
    count = 1
    high_scores = retrieve(rangestr)
    print(f'{rangestr}:')
    for user in high_scores:
        print(count,".",user, ":",high_scores[user])
        count += 1
        if count > 11:
            break
    else:
        input("Enter anything to continue")
        return


def print_reactionspeed_leaderboard():
    from retrieve_high_scores import retrieve_reaction_speed as retrieve 
    count = 1
    high_scores = retrieve()
    for user in high_scores:
        print(count,".",user, ":",high_scores[user])
        count += 1
        if count > 11:
            break
    else:
        input("Enter anything to continue")
        return


def choose_leaderboard():
    while True:
        choice = int(input("What leaderboard would you like to see?\nPress 1 for Tic Tac Toe\nPress 2 for Number Guessing Game\nPress 3 for Reaction Speed Game\nPress 4 to leave leaderboards\n:"))
        if choice == 1:
            print_tictactoe_leaderboard()
        elif choice == 2:
            print_numguessing_leaderboard('1-10')
            print_numguessing_leaderboard('1-100')
            print_numguessing_leaderboard('1-1000')
        elif choice == 3:
            print_reactionspeed_leaderboard()
        elif choice == 4:
            return
        else:
            print("You didn't put in one of the given numbers!")
            continue


#-------------------------------------------------------------------------------------------End of Matthew's Code-------------------------------------------------------------------------------------------#