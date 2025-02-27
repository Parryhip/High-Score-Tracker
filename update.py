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





# Updates the high score for Tic-Tac-Toe
def update_tic_tac_toe_high_score(username, new_score):
    if username == "anonymous":
        return  # Anonymous users don't get high scores

    high_scores = {}
    filename = "tic_tac_toe_high_scores.txt"

    # Read existing high scores
    try:
        with open(filename, "r") as file:
            for line in file:
                user, score = line.strip().split(":")
                high_scores[user] = int(score)
    except FileNotFoundError:
        pass  # If file doesn't exist, treat it as empty

    # Update if new score is higher
    if username not in high_scores or new_score > high_scores[username]:
        high_scores[username] = new_score

        # Write updated high scores back to file
        with open(filename, "w") as file:
            for user, score in high_scores.items():
                file.write(f"{user}:{score}\n")


# Updates the high score for the Number Guessing Game (lower scores are better)
def update_num_guessing_high_score(username, new_score):
    if username == "anonymous":
        return  # Anonymous users don't get high scores

    high_scores = {}
    filename = "num_guessing_high_scores.txt"

    # Read existing high scores
    try:
        with open(filename, "r") as file:
            for line in file:
                user, score = line.strip().split(":")
                high_scores[user] = int(score)
    except FileNotFoundError:
        pass  # If file doesn't exist, treat it as empty

    # Update if new score is lower (fewer guesses = better score)
    if username not in high_scores or new_score < high_scores[username]:
        high_scores[username] = new_score

        # Write updated high scores back to file
        with open(filename, "w") as file:
            for user, score in high_scores.items():
                file.write(f"{user}:{score}\n")


# Updates the high score for the Reaction Speed Game (lower times are better)
def update_reaction_speed_high_score(username, new_time):
    if username == "anonymous":
        return  # Anonymous users don't get high scores

    high_scores = {}
    filename = "reaction_speed_high_scores.txt"

    # Read existing high scores
    try:
        with open(filename, "r") as file:
            for line in file:
                user, score = line.strip().split(":")
                high_scores[user] = float(score)  # Reaction time is a float (seconds)
    except FileNotFoundError:
        pass  # If file doesn't exist, treat it as empty

    # Update if new time is lower (faster reaction = better score)
    if username not in high_scores or new_time < high_scores[username]:
        high_scores[username] = new_time

        # Write updated high scores back to file
        with open(filename, "w") as file:
            for user, score in high_scores.items():
                file.write(f"{user}:{score}\n")


#------------------------------------------------------------------------End of D Code-------------------------------------------------------------------------

