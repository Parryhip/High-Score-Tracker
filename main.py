from sign_in_func import *
from games import *
from update import *
from display_highscores import *
#Main function to access games and leaderboard
def main_ui():
    print("Welcome to your high score tracker!\nHere you can play some games, and have your scores recorded on a leaderboard!")
    #Checks to make sure the user made it through the sign in process
    signed_in = sign_in()
    if signed_in == 'exit':
        print("Goodbye!")
        exit()
    else:
        username = signed_in
    #Allows the user to access the games, leaderboard, or exit the program
    while True:
        choice = input("What would you like to do?\n1:Play a game\n2:View leaderboard\n3:Leave\n").strip()
        if choice == '1':
            game_ui(username)
        elif choice == '2':
            choose_leaderboard()
        elif choice == '3':
            print("Goodbye!")
            exit()
main_ui()