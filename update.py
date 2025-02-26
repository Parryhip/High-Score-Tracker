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
                    username = input("What is your username?(or type exit to exit)\n-->")
                    if username.lower() == "exit":
                        go_to_first_choice = True
                        break
                    with open("login_info.txt", "r") as file:
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
                    password = input("What is your password?(or type exit to exit)\n-->")
                    if password.lower() == "exit":
                        go_to_first_choice = True
                        break
                    with open("login_info.txt", "r") as file:
                        for line in file:
                            items = line.split(":")
                            if username == items[0]:
                                if password == items[1]:
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
                username = input("What is the username that you want to create?\n-->")
                if username.lower() == "exit":
                    print("Don't use that username please.")
                    continue
                with open("login_info.txt", "r") as file:
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
                password = input("What is the password that you want to create?\n-->")
                if password.lower() == "exit":
                    print("Don't use that password please.")
                    continue
                confirm_password = input("Please type your password again to confirm.\n-->")
                if password == confirm_password:
                    print("Username of",username,"and password of",password,"has been inputted successfully!")
                    with open("login_info.txt", "a") as file:
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



#------------------------------------------------------------------------Daniel Code---------------------------------------------------------------------------
def update_high_score(username, new_score):
    """Updates the user's high score if the new score is higher than the previous one."""
    if username == "anonymous":
        return  # Do not update scores for anonymous users
    
    updated_lines = []
    user_found = False
    
    # Read and update high score
    with open("high_scores.txt", "r") as file:
        for line in file:
            stored_username, stored_score = line.strip().split(":")
            stored_score = int(stored_score)
            
            if stored_username == username:
                user_found = True
                if new_score > stored_score:
                    updated_lines.append(f"{username}:{new_score}\n")  # Update with new high score
                else:
                    updated_lines.append(line)  # Keep existing score
            else:
                updated_lines.append(line)
    
    if not user_found:  # If user is new, add them to the high score file
        updated_lines.append(f"{username}:{new_score}\n")
    
    # Write updated high scores back to the file
    with open("high_scores.txt", "w") as file:
        file.writelines(updated_lines)

def update_leaderboard():
    """Updates the leaderboard based on the latest high scores."""
    with open("high_scores.txt", "r") as file:
        scores = [line.strip().split(":") for line in file]

    # Convert scores to integers and sort in descending order
    scores = [(username, int(score)) for username, score in scores]
    scores.sort(key=lambda x: x[1], reverse=True)  # Sort by high score

    # Write the sorted leaderboard
    with open("leaderboard.txt", "w") as file:
        for rank, (username, score) in enumerate(scores, start=1):
            file.write(f"{rank}. {username}: {score}\n")



#------------------------------------------------------------------------End of D Code------------------------------------------------------------------------