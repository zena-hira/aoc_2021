from collections import Counter, defaultdict


def crabs_1(l):
    ns = list(map(int, l[0].split(',')))
    hi = max(ns)
    c = Counter(ns)
    vs = defaultdict(int)
    for i in range(hi+1):
        for k,v in c.items():
            vs[i] += abs(k-i) * v

    return vs[min(vs, key=vs.get)]


def crabs_2(l):
    ns = list(map(int, l[0].split(',')))
    hi = max(ns)
    c = Counter(ns)
    vs = defaultdict(int)
    for i in range(hi + 1):
        for k, v in c.items():
            vs[i] += sum(range(0, abs(k - i)+1)) * v

    return vs[min(vs, key=vs.get)]


