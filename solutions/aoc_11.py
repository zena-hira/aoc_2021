def Octopus_1(l):
    grid = mkGrid(l)
    total_flashes = simulate(grid)
    return total_flashes

def simulate(grid, n=100):
    totalFlashes = 0
    for round in range(0, n):
        todo = []
        flashed = {}
        nextGrid = mkEmptyGrid()
        for i in range(0, 10):
            for j in range(0, 10):
                nextGrid[i][j] += (grid[i][j] + 1)
                if nextGrid[i][j] > 9:
                    todo.append((i,j)) #to flush

        while len(todo) > 0:
            i,j = todo.pop()
            if (i,j) in flashed:
                continue
            flashed[(i,j)] = True
            for ni,nj in neighbours(i,j):
                nextGrid[ni][nj] += 1
                if nextGrid[ni][nj] > 9:
                    todo.append((ni,nj))

        for (i,j) in flashed.keys():
            nextGrid[i][j] = 0

        totalFlashes += len(flashed)
        if len(flashed) == 100:
            return round

        grid = nextGrid
    return totalFlashes

def neighbours(i,j):
    for ni in (i + x for x in [-1,0,1]):
        for nj in (j + x for x in [-1, 0, 1]):
            if ni < 0 or ni >= 10 or nj < 0 or nj >= 10 or (ni == i and nj == j):
                continue
            else:
                yield (ni, nj)



def mkEmptyGrid():
    return [ [0 for i in range(0,10)] for j in range(0,10)]

def mkGrid(l):
    return [[ int(c) for c in line] for line in l]

def Octopus_2(l):
    grid = mkGrid(l)
    flash_together = simulate(grid,9999999999)
    return flash_together+1