#------------------------------------------------------------------------Daniel Code---------------------------------------------------------------------------
def update_high_score(username, new_score):
    """Updates the user's high score if the new score is higher than the previous one."""
    if username == "anonymous":
        return  # Do not update scores for anonymous users
    
    updated_lines = []
    user_found = False
    
    # Read and update high score
    with open("High-Score-Tracker\high_scores.txt", "r") as file:
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



#------------------------------------------------------------------------End of D Code-------------------------------------------------------------------------