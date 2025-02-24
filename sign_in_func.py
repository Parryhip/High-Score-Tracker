#Samuel Andelin, Sign in function, High Score Tracker

#list holding all user login information
user_info = []

#read function
def read():
    with open("login_info.txt", "r") as file:
        for line in file:
            user_info.append(line)

#sign in function
def sign_in():
    while True:
        choice = input("Type 1 to sign in, type 2 to sign up, and type 3 to exit.")
        if choice == "1":
            while True:
                username = input("What is your username?\n-->")
                with open("login_info.txt", "r") as file:
                    for line in file:
                        pass

