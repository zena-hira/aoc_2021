from collections import defaultdict

part1_target = (frozenset([(2,3), (3,3)]), frozenset([(2,5), (3,5)]), frozenset([(2,7), (3,7)]), frozenset([(2,9), (3,9)]))
targets = {'A': 3, 'B': 5, 'C': 7, 'D':9}
costs = {'A':1, 'B':10, 'C':100, 'D':1000}

def amphipod_1(l):
    grid = parse(l)
    seen = {}
    amphi_dict = find_amphis(grid)
    solve(amphi_dict, 0, seen)
    return seen[part1_target]


def find_amphis(grid):
    amphi_dict = defaultdict(set)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'A':
                amphi_dict['A'].add((i,j))
            elif grid[i][j] == 'B':
                amphi_dict['B'].add((i, j))
            elif grid[i][j] == 'C':
                amphi_dict['C'].add((i, j))
            elif grid[i][j] == 'D':
                amphi_dict['D'].add((i, j))
    for k in amphi_dict.keys():
        amphi_dict[k] = frozenset(amphi_dict[k])
    return amphi_dict

def freeze(amphi_dict):
    return (amphi_dict['A'], amphi_dict['B'], amphi_dict['C'], amphi_dict['D'])


def solved(f):
    return f == part1_target

def hallway(blocked, position):

    for i in range(position[1] - 1, 0, -1):
        if (1,i) not in blocked:
            if i in [3, 5, 7, 9]:
                continue
            else:
                yield (1, i), position[1] - i
        else:
            break
    for i in range(position[1] + 1, 12):
        if (1,i) not in blocked:
            if i in [3, 5, 7, 9]:
                continue
            else:
                yield (1, i), i - position[1]
        else:
            break

def reachable(position, blocked, amphi, amphi_dict):
    target_col = targets[amphi]
    if (position[1] == target_col and position[0] == 3) or (position[1] == target_col and position[0] == 2 and (3, target_col) in amphi_dict[amphi]):
        return

    if position[0] == 2:
        if (1,position[1]) in blocked:
            return
        else:
            for p, c in hallway(blocked, position):
                yield p, c+1
    if position[0] == 3:
        if (1,position[1]) in blocked or (2,position[1]) in blocked:
            return
        else:
            for p, c in hallway(blocked, position):
                yield p, c + 2

    if position[0] == 1:
        target_col = targets[amphi]
        if not any([(1, i) in blocked for i in range(min(position[1], target_col), max(position[1], target_col)+1)]):
            if (2, target_col) in blocked:
                pass
            elif (3, target_col) in blocked:
                if (3, target_col) in amphi_dict[amphi]:
                    yield (2, target_col), 1 + abs(position[1] - target_col)
            else:
                yield (3, target_col), 2 + abs(position[1] - target_col)

def next_moves(amphi_dict, score):
    blocked = set()
    for val in amphi_dict.values():
        blocked.update(val)
    for amphi, ps in amphi_dict.items():
        for position in ps:
            for next_p, distance in reachable(position, blocked - set([position]), amphi, amphi_dict):
                next_ad = dict(amphi_dict)
                next_ad[amphi] = (amphi_dict[amphi] - {position}) | {next_p}
                next_score = score + distance * costs[amphi]
                yield next_ad, next_score


def solve(amphi_dict, score, seen):

    f = freeze(amphi_dict)
    if f in seen and seen[f] <= score:
        return
    seen[f] = score

    if solved(f):
        return

    for next_amphi_dict, next_score in next_moves(amphi_dict, score):
        solve(next_amphi_dict, next_score, seen)

def parse(l):
    grid = []
    for line in l:
        grid.append([c for c in line])
    return grid


def amphipod_2(l):
    grid = parse(l)
    extras = [[i for i in "  #D#C#B#A#  "]
             ,[i for i in "  #D#B#A#C#  "]
             ]
    grid = grid[0:3] + extras + grid[3:]

    seen = {}
    amphi_dict = find_amphis(grid)
    solve_2(amphi_dict, 0, seen)
    return seen[part2_target]



part2_target = (frozenset([(2,3), (3,3), (4,3), (5,3)]), frozenset([(2,5), (3,5), (4,5), (5,5)]),
                frozenset([(2,7), (3,7), (4,7), (5,7)]), frozenset([(2,9), (3,9), (4,9), (5,9)]))


def reachable_2(position, blocked, amphi, amphi_dict):
    target_col = targets[amphi]

    # check we're in a sorted column and don't need to move
    if (position[1]) == target_col and position[0] >= 2:
        for i in range(5, position[0], -1):
            if (i, target_col) not in amphi_dict[amphi]:
                break
        else:
            return

    # we're in an unsorted column and can move to the hallway
    for i in [2,3,4,5]:
        if position[0] == i:
            if any((j, position[1]) in blocked for j in range(1,i)):
                return
            else:
                for p, c in hallway(blocked, position):
                    yield p, c+(i-1)

    # we're in the hallway
    if position[0] == 1:
        target_col = targets[amphi]
        if not any((1, i) in blocked for i in range(min(position[1], target_col), max(position[1], target_col)+1)):
            max_pos = None
            for i in range(2,6):
                if (i, target_col) in blocked:
                    if (i, target_col) in amphi_dict[amphi]:
                        continue
                    else:
                        return
                else:
                    max_pos = i
            yield (max_pos, target_col), (max_pos - 1) + abs(position[1] - target_col)


def solve_2(amphi_dict, score, seen):

    f = freeze(amphi_dict)
    if f in seen and seen[f] <= score:
        return seen[f]
    seen[f] = score

    if solved(f):
        return score

    for next_amphi_dict, next_score in next_moves_2(amphi_dict, score):
        solve_2(next_amphi_dict, next_score, seen)


def next_moves_2(amphi_dict, score):
    blocked = set()
    for val in amphi_dict.values():
        blocked.update(val)
    for amphi, ps in amphi_dict.items():
        for position in ps:
            for next_p, distance in reachable_2(position, blocked - {position}, amphi, amphi_dict):
                next_ad = dict(amphi_dict)
                next_ad[amphi] = (amphi_dict[amphi] - {position}) | {next_p}
                next_score = score + distance * costs[amphi]
                yield next_ad, next_score
