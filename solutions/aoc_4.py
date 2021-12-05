import numpy as np


def calculate_score(board, striked_numbers, n):
    return n * sum([item for row in board for item in row if item not in striked_numbers])


def bingo_1(l):
    numbers, boards = parse(l)

    striked_numbers = set([])
    for n in numbers:
        striked_numbers.add(n)
        for b in boards:
            if is_complete(b, striked_numbers):
                return calculate_score(b, striked_numbers, n)


def parse(l):
    numbers = map(int, l[0].split(','))
    current_board = []
    boards = [current_board]

    for row in l[2:]:
        if row == '':
            current_board = []
            boards.append(current_board)
        else:
            current_board.append(list(map(int, row.split())))

    return numbers, boards


def is_complete(board, striked_numbers):
    for row in board:
        if set(row).issubset(striked_numbers):
            return True
    
    for col in np.array(board).T:
        if set(col).issubset(striked_numbers):
            return True
    
    return False
    
    
def bingo_2(l):
    numbers, boards = parse(l)

    striked_numbers = set([])
    for n in numbers:
        striked_numbers.add(n)
        next_boards = []
        for b in boards:
            if not (is_complete(b, striked_numbers)):
                next_boards.append(b)

            if len(boards) == 1 and is_complete(b, striked_numbers):
                return calculate_score(b, striked_numbers, n)
        boards = next_boards
    return None
