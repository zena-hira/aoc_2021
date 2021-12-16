import heapq


def chiton_1(l):
    grid = parse(l)
    return search2(grid)

def neighbours(p, grid):
    x,y = p
    for a,b in [(-1,0), (1,0), (0,-1), (0,1)]:
        if x+a >= 0 and x+a < len(grid) and y+b >= 0 and y+b < len(grid):
            yield ((x+a), (y+b))


def search2(grid):
    limiter = set()

    endVal = len(grid) - 1

    stack = []
    # pick position with least cost
    heapq.heappush(stack, (0, (0,0)))

    while len(stack) > 0:
        (cost, position) = heapq.heappop(stack)
        # if we have been here before with less cost -> stop
        if position in limiter:
            continue
        limiter.add(position)

        if position == (endVal, endVal):
            return cost

        for (nx, ny) in neighbours(position, grid):
            if (nx, ny) in limiter:
                continue
            heapq.heappush(stack, (cost + grid[nx][ny], (nx,ny)))


def parse(l):
    return list(list(int(c) for c in line) for line in l)

def chiton_2(l):
    grid = parse(l)
    out = []

    for ex in grid:
        ex2 = []
        out.append(ex2)
        for i in range(0, 5):
            for ey in ex:
                ex2.append(wrap(ey, i))

    out2 = []
    for i in range(0,5):
        for ex in out:
            ex2 = []
            out2.append(ex2)
            for ey in ex:
               ex2.append(wrap(ey, i))

    #for row in out2:
    #    print(''.join(str(x) for x in row))

    return search2(out2)

def wrap(x,i):
    if (x+i) <= 9:
        return x+i

    return (x+i) - 9