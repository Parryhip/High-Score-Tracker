#Samuel Andelin, Retrieve high scores function

def sort_by(item):
    try:
        return round(int(item[1]), 2)
    except:
        return round(float(item[1]), 2)

def retrieve_tic_tac_toe():
    list_with_highscores_to_sort = []
    with open("tic_tac_toe_high_scores.txt", "r") as file:
        for line in file:
            items = line.split(":")
            list_with_highscores_to_sort.append((items[0], items[1]))
    list_with_highscores_to_sort.sort(key=sort_by)
    dictionary_with_high_scores = {}
    for item in list_with_highscores_to_sort:
        dictionary_with_high_scores[item[0]] = item[1]
    return dictionary_with_high_scores

def retrieve_num_guessing():
    list_with_highscores_to_sort = []
    with open("num_guessing_high_scores.txt", "r") as file:
        for line in file:
            items = line.split(":")
            list_with_highscores_to_sort.append((items[0], items[1]))
    list_with_highscores_to_sort.sort(key=sort_by)
    dictionary_with_high_scores = {}
    for item in list_with_highscores_to_sort:
        dictionary_with_high_scores[item[0]] = item[1]
    return dictionary_with_high_scores

def retrieve_reaction_speed():
    list_with_highscores_to_sort = []
    with open("reaction_speed_high_scores.txt", "r") as file:
        for line in file:
            items = line.split(":")
            list_with_highscores_to_sort.append((items[0], round(float(items[1]), 2)))
    list_with_highscores_to_sort.sort(key=sort_by)
    dictionary_with_high_scores = {}
    for item in list_with_highscores_to_sort:
        dictionary_with_high_scores[item[0]] = item[1]
    return dictionary_with_high_scores