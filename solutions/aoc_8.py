import itertools
from collections import defaultdict, Counter

def segment_1(l):
    info = parse(l)
    counts = defaultdict(int)

    for pre, post in info:
        cs = Counter(map(len, post))
        counts[1] += cs[2]
        counts[4] += cs[4]
        counts[7] += cs[3]
        counts[8] += cs[7]

    return sum(counts.values())


def parse(l):
    res = []
    for line in l:
        pre, post = line.split(" | ")
        res.append([pre.split(), post.split()])
    return res


shapes = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}

# i am sure there are easier ways to do this part
def segment_2(l):
    info = parse(l)

    running_sum = 0
    for pre, post in info:
        wires_options = defaultdict(set)

        for wires in pre:
            wires_options[len(wires)].add(wires)
        mapping = solve(wires_options)

        v = 0
        for numberWires in post:
            v = (v * 10) + (mapping[''.join(sorted(numberWires))])
        running_sum += v

    return running_sum


def solve(wires_options):
    order = [1,4,7,0,2,3,5,6,9,8]

    def solve_aux(index, mapping_so_far):
        if index == 10:
            return mapping_so_far
        current_num = order[index]
        letters = shapes[current_num]

        possibles = wires_options[len(letters)]

        for p in possibles:
            for perm in itertools.permutations(p):
                new_map = { k:v for k,v in zip(letters, perm)} #build map from original to mapping
                perm_ok = True
                for (k,v) in new_map.items():
                    if k in mapping_so_far.keys() and mapping_so_far[k] != v:
                        perm_ok = False
                        break
                if perm_ok:
                    next = new_map.copy()
                    next.update(mapping_so_far)
                    r = solve_aux(index+1, next)
                    if r is not None:
                        return r

        return None

    inner_map = solve_aux(0, {})

    outer_map = {}
    # maps seq of letters to shape number e.g abcefg -> 0
    for k,v in shapes.items():
        outer_map[''.join(sorted(inner_map[x] for x in v))] = k
    return outer_map

