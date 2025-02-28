#Samuel Andelin, Retrieve high scores function

def sort_by(item):
    return int(item[1])

def sort_by_float(item):
    return float(item[1])

def retrieve_tic_tac_toe():
    list_with_highscores_to_sort = []
    with open("High-Score-Tracker/tic_tac_toe_high_scores.txt", "r") as file:
        for line in file:
            items = line.split(":")
            list_with_highscores_to_sort.append((items[0], items[1]))
    list_with_highscores_to_sort.sort(key=sort_by, reverse=True)
    dictionary_with_high_scores = {}
    for item in list_with_highscores_to_sort:
        dictionary_with_high_scores[item[0]] = item[1]
    return dictionary_with_high_scores

def retrieve_num_guessing(rangestr):
    list_with_highscores_to_sort = []
    with open("High-Score-Tracker/num_guessing_high_scores.txt", "r") as file:
        for line in file:
            items = line.split(":")
            if items[2] == rangestr+'\n':
                list_with_highscores_to_sort.append((items[0], items[1]))
    list_with_highscores_to_sort.sort(key=sort_by)
    dictionary_with_high_scores = {}
    for item in list_with_highscores_to_sort:
        dictionary_with_high_scores[item[0]] = item[1]
    return dictionary_with_high_scores

def retrieve_reaction_speed():
    list_with_highscores_to_sort = []
    with open("High-Score-Tracker/reaction_speed_high_scores.txt", "r") as file:
        for line in file:
            items = line.split(":")
            list_with_highscores_to_sort.append((items[0], items[1]))
    list_with_highscores_to_sort.sort(key=sort_by_float)
    dictionary_with_high_scores = {}
    for item in list_with_highscores_to_sort:
        dictionary_with_high_scores[item[0]] = item[1]
    return dictionary_with_high_scores