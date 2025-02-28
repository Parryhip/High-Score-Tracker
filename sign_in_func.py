#Samuel Andelin, Sign in function, High Score Tracker

#sign in function
def sign_in():
    while True:
        choice = input("Type 1 to sign in, type 2 to sign up, type 3 to be anonymous, and type 4 to exit.\n-->")
        if choice == "1":
            while True:
                go_to_first_choice = False
                while True:
                    loopback = True
                    username = input("What is your username?(or type exit to exit)\n-->").strip()
                    if username.lower() == "exit":
                        go_to_first_choice = True
                        break
                    with open("High-Score-Tracker/login_info.txt", "r") as file:
                        for line in file:
                            items = line.split(":")
                            if username == items[0]:
                                loopback = False
                                break
                    if loopback:
                        print("Username not found!!!")
                        continue
                    else:
                        break
                if go_to_first_choice:
                    break
                while True:
                    loopback = True
                    password = input("What is your password?(or type exit to exit)\n-->").strip()
                    if password.lower() == "exit":
                        go_to_first_choice = True
                        break
                    with open("High-Score-Tracker/login_info.txt", "r") as file:
                        for line in file:
                            items = line.split(":")
                            if username == items[0]:
                                if password == items[1] or f'{password}\n' == items[1]:
                                    print("Signed in successfully!")
                                    return username
                                else:
                                    print("Invalid password!")
                                    break

                    if loopback:
                        continue
                if go_to_first_choice:
                    break
                
        elif choice == "2":
            while True:
                loopback = False
                username = input("What is the username that you want to create?\n-->").strip()
                if username.lower() == "exit":
                    print("Don't use that username please.")
                    continue
                with open("High-Score-Tracker/login_info.txt", "r") as file:
                    for line in file:
                        items = line.split(":")
                        if username == items[0]:
                            print("Username is already taken!")
                            loopback = True
                if loopback:
                    continue
                else:
                    break
            while True:
                password = input("What is the password that you want to create?\n-->").strip()
                if password.lower() == "exit":
                    print("Don't use that password please.")
                    continue
                confirm_password = input("Please type your password again to confirm.\n-->")
                if password == confirm_password:
                    print("Username of",username,"and password of",password,"has been inputted successfully!")
                    with open("High-Score-Tracker/login_info.txt", "a") as file:
                        file.write("\n")
                        file.write(username+":"+password)
                    break
                else:
                    print("Passwords do not match!!!")
                    continue
        elif choice == "3":
            return "anonymous"
        elif choice == "4":
            return "exit"
        else:
            print("Not a valid option!")
