#Nicholas Larsen

def match(board, letter):
    for row in board:
        matched = True
        for collumn in row:
            if collumn != letter:
                matched = False
        if matched:
            return True
        #uses range to select the correct indexes in the correct rows to find vertical matches
    for collumn in range(3):
        matched = True
        for row in board:
            if row[collumn] != letter:
                matched = False
        if matched:
            return True
    matched = True
    for square in range(3):
        if board[square][square] != letter:
            matched = False
        

        