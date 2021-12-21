import itertools
from collections import Counter
from functools import cache


def dirac_1(l):
    positions = parse(l)
    dice = itertools.cycle(range(1, 101))
    current = 0
    scores = [0,0]
    die_counter = 0
    while True:
        roll = next(dice) + next(dice) + next(dice)
        die_counter += 3
        positions[current] += roll % 10
        if positions[current] > 10:
            positions[current] -= 10
        scores[current] += positions[current]
        if scores[current] >= 1000:
            break
        current += 1
        current = current % 2
    return min(scores) * die_counter

def parse(l):
    positions = []
    for line in l:
        positions.append(int(line.split(':')[1]))
    return positions


def star_2_aux(player_1_score, player_2_score, roll, position_1, position_2):
    position_1 += roll
    if position_1 > 10:
        position_1 -= 10
    player_1_score += position_1
    if player_1_score >= 21:
        return 1, 0
    p2_u, p1_u = try_next(player_2_score, player_1_score, position_2, position_1)
    return p1_u, p2_u

dice_score = Counter(map(sum, itertools.product(range(1, 4), repeat = 3)))
@cache
def try_next(p1_s, p2_s, p1_p, p2_p):
    p1_u = 0
    p2_u = 0
    for score, freq in dice_score.items():
        p1_r, p2_r = star_2_aux(p1_s, p2_s, score, p1_p, p2_p)
        p1_u += p1_r * freq
        p2_u += p2_r * freq
    return p1_u, p2_u

def dirac_2(l):
    positions = parse(l)
    p1,p2 = try_next(0, 0, positions[0], positions[1])
    return max(p1, p2)
