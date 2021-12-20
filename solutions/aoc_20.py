def star_1(l):
    translation, sparse, translation_neg = parse(l)
    if translation[0]:
        next_points = next_sparse(translation_neg, sparse)
        next_points = next_sparse(translation, next_points, invert = True)

    else:
        next_points = next_sparse(translation, sparse)
        next_points = next_sparse(translation, next_points)
    return len(next_points)

def parse(l):
    translation = [el == '#' for el in l[0]]
    translation_neg = [el == '.' for el in l[0]]

    sparse = set()
    for j in range(len(l)-2):
        for i in range(len(l[j+2])):
            if l[j+2][i] == '#':
                sparse.add((i,j))

    return translation, sparse, translation_neg

def get_neighbours(i,j):
    return [(i-1, j-1), (i, j-1), (i+1, j-1),
            (i-1, j), (i, j), (i+1, j),
            (i-1, j+1), (i, j+1), (i+1, j+1)]


def next_sparse(translation, sparse, invert = False):
    points_to_check = set()
    next_points = set()
    for p in sparse:
        i, j = p
        points_to_check.update(get_neighbours(i,j))

    for p in points_to_check:
        i,j = p
        x = [neighbour in sparse for neighbour in get_neighbours(i, j)]
        if invert:
            x = [not el for el in x]
        if translation[int(''.join([str(int(y)) for y in x]), 2)]:
            next_points.add((i,j))
    return next_points




def star_2(l):
    translation, sparse, translation_neg = parse(l)
    next_points = sparse
    for _ in range(0, 25):
        if translation[0]:
            next_points = next_sparse(translation_neg, next_points)
            next_points = next_sparse(translation, next_points, invert=True)

        else:
            next_points = next_sparse(translation, next_points)
            next_points = next_sparse(translation, next_points)

    return len(next_points)
