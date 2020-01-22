MOVES = {
    0: (-2, -1),
    1: (-1, -2),
    2: (1, -2),
    3: (2, -1),
    4: (2, 1),
    5: (1, 2),
    6: (-1, 2),
    7: (-2, 1)
}


def nextMove(x, y, i):
    xi, yi = MOVES[i]
    return x + xi, y + yi