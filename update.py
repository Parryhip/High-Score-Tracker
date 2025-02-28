#------------------------------------------------------------------------Daniel Code---------------------------------------------------------------------------

# Updates the high score for Tic-Tac-Toe
def update_tic_tac_toe_high_score(username):
    if username == "anonymous":
        return  # Anonymous users don't get high scores

    filename = "High-Score-Tracker/tic_tac_toe_high_scores.txt"

    # Read existing high scores
    high_scores = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                user, score = line.strip().split(":")
                high_scores[user] = int(score)
    except FileNotFoundError:
        pass  # If file doesn't exist, treat it as empty

    # Replace old score with the new one 
    high_scores[username] = high_scores.get(username, 0)

    # Write updated high scores back to file
    with open(filename, "w") as file:
        for user, score in high_scores.items():
            file.write(f"{user}:{score}\n")

# Updates the high score for the Number Guessing Game (lower scores are better)
def update_num_guessing_high_score(username, new_score, range):
    if username == "anonymous":
        return  # Anonymous users don't get high scores

    high_scores = {}
    filename = "High-Score-Tracker/num_guessing_high_scores.txt"

    # Read existing high scores
    try:
        with open(filename, "r") as file:
            for line in file:
                user, score, rangestr = line.strip().split(":")
                if not user in high_scores:
                    high_scores[user] = {}
                high_scores[user][rangestr] = int(score)
    except FileNotFoundError:
        pass  # If file doesn't exist, treat it as empty

    # Update if new score is lower (fewer guesses = better score)
    new_range = f'{range[0]}-{range[1]}'
    if username not in high_scores or new_range not in high_scores[username] or new_score < high_scores[username][new_range]:
        if not username in high_scores:
            high_scores[username] = {}
        high_scores[username][new_range] = new_score

        # Write updated high scores back to file
        with open(filename, "w") as file:
            for user, scores in high_scores.items():
                for rangestr, score in scores.items():
                    file.write(f"{user}:{score}:{rangestr}\n")


# Updates the high score for the Reaction Speed Game (lower times are better)
def update_reaction_speed_high_score(username, new_time):
    if username == "anonymous":
        return  # Anonymous users don't get high scores

    high_scores = {}
    filename = "High-Score-Tracker/reaction_speed_high_scores.txt"

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