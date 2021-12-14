from collections import Counter


def polymerization_1(l):
    start, rules = parse(l)

    current = start
    for i in range(0, 10):
        current = step(current, rules)

    c = Counter(current)
    mv = min(v for k,v in c.items())
    maxv = max(v for k,v in c.items())
    return (maxv - mv)

def step(current, rules):
    next = []
    for a,b in zip(current, current[1:]):
        next.append(a)
        next.append(rules[a + b])
    next.append(current[-1])
    return next

def parse(l):
    start = l[0]
    rules = {}
    for line in l[2:]:
        pre, post = line.split(" -> ")
        rules[pre] = post
    return start, rules


def step2(a, b, rules, depth, memo):
    if (a,b,depth) in memo:
        return memo[(a,b,depth)]

    if depth == 0:
        return Counter({a: 1})

    mid = rules[a+b]
    d1 = step2(a, mid, rules, depth-1, memo)
    d2 = step2(mid, b, rules, depth-1, memo)
    r = d1 + d2
    memo[a,b,depth] = r
    return r

def polymerization_2(l):
    start, rules = parse(l)
    memo = {}
    c = Counter()
    for a,b in zip(start, start[1:]):
        c = c + step2(a,b, rules, 40, memo)
    c[start[-1]] += 1

    mv = min(v for k,v in c.items())
    maxv = max(v for k,v in c.items())
    return (maxv - mv)