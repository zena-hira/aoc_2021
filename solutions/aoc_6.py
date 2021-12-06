
from collections import Counter, defaultdict


def lanternfish(l, days):
    numbers = map(int, l[0].split(','))

    c = Counter(numbers)

    for day in range(days):
        c2 = defaultdict(int)
        for k,v in c.items():
            if k == 0:
                c2[6] += v
                c2[8] += v
            else:
                c2[k-1] += v
        c = c2

    return sum(c.values())

