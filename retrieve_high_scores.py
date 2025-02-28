#Samuel Andelin, Retrieve high scores function

#sorting key for sorting the list of scroes for the leaderboard
def sort_by(item):
    #Tries to give back a integer value, if it can't, return a float (just in case)
    try:
        return round(int(item[1]), 2)
    except:
        return round(float(item[1]), 2)

#function for sorting by a float
def sort_by_float(item):
    return float(item[1])

#gets high scores for tic tac toe, sorts them, and returns them
def retrieve_tic_tac_toe():
    #creates a list to sort
    list_with_highscores_to_sort = []

    #opens tic tac toe high scores file to read
    with open("tic_tac_toe_high_scores.txt", "r") as file:
        #iterates over items in the file
        for line in file:
            #splits the items into a readable form
            items = line.split(":")
            #appends the highscore with the username
            list_with_highscores_to_sort.append((items[0], items[1]))

    #sorts the list using a key AND reverses it
    list_with_highscores_to_sort.sort(key=sort_by, reverse=True)

    #dictionary to return with sorted high scores
    dictionary_with_high_scores = {}

    #iterates over the sorted high scores and puts them into the dictionary
    for item in list_with_highscores_to_sort:
        dictionary_with_high_scores[item[0]] = item[1]

    #returns the high scores
    return dictionary_with_high_scores

#gets high scores for number guessing game, sorts them, and returns them
def retrieve_num_guessing(rangestr):
    #creates a list to sort
    list_with_highscores_to_sort = []

    #opens number guessing high scores file to read
    with open("num_guessing_high_scores.txt", "r") as file:
        #iterates over items in the file
        for line in file:
            #splits the items into a readable form
            items = line.split(":")

            #if the third item in the line is a range, append the high score of that range
            if items[2] == rangestr+'\n':
                list_with_highscores_to_sort.append((items[0], items[1]))

    #sorts the list using a key
    list_with_highscores_to_sort.sort(key=sort_by)

    #dictionary to return with sorted high scores
    dictionary_with_high_scores = {}

    #iterates over the sorted high scores and puts them into the dictionary
    for item in list_with_highscores_to_sort:
        dictionary_with_high_scores[item[0]] = item[1]

    #returns the high scores
    return dictionary_with_high_scores

#gets high scores reaction speed game, sorts them, and returns them
def retrieve_reaction_speed():
    #creates a list to sort
    list_with_highscores_to_sort = []

    #opens reaction speed high scores file to read
    with open("reaction_speed_high_scores.txt", "r") as file:
        #iterates over items in the file
        for line in file:
            #splits the items into a readable form
            items = line.split(":")
            #appends the highscore with the username
            list_with_highscores_to_sort.append((items[0], items[1]))

    #sorts the list using a key
    list_with_highscores_to_sort.sort(key=sort_by_float)

    #dictionary to return with sorted high scores
    dictionary_with_high_scores = {}

    #iterates over the sorted high scores and puts them into the dictionary
    for item in list_with_highscores_to_sort:
        dictionary_with_high_scores[item[0]] = item[1]
    
    #returns the high scores
    return dictionary_with_high_scores