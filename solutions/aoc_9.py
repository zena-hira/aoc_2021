def basins_1(l):
    min_points = []
    for i in range(0, len(l)):
        for j in range(0, len(l[i])):
            #print(i, j, l[i][j])
            #print(list(neighbours(l, i,j)))
            if int(l[i][j]) < min(list(int(l[a][b]) for (a,b) in neighbours(l,i,j))):
                #print(l[i][j])
                min_points.append(int(l[i][j]))
    return (sum(a+1 for a in min_points))


def neighbours(l,i,j):
    for (x,y) in [(-1,0), (1,0), (0,-1), (0,1)]:
        if (i+x) >= 0 and i+x < len(l) and (y+j >= 0) and y+j < len(l[i+x]):
            yield (x+i,j+y)


def basins_2(l):
    l = list((list(line) for line in l))

    basins = []
    for i in range(0, len(l)):
        for j in range(0, len(l[i])):
            c = l[i][j]
            if c == 'X' or c == '9':
                continue
            else:
                basins.append(flood(l,i,j))
    a,b,c, *rest = sorted(basins, reverse= True)
    return a*b*c


def flood(l, i, j):
    q = [(i,j)]
    t = 0
    while len(q) > 0:
        (x,y) = q.pop()
        c = l[x][y]
        if c == 'X' or c == '9':
            continue
        t += 1
        l[x][y] = 'X'
        q += list(neighbours(l,x,y))
    return t
