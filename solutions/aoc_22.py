def reactor_1(l):
    status = parse(l)
    return run_with_bounds(status, -50, 50)

def run_with_bounds(status, min_bounds, max_bounds):
    coordinates = set()
    for inst,x,y,z in status:
        xl, xh = x
        yl, yh = y
        zl, zh = z
        xl = max(xl, min_bounds)
        xh = min(xh, max_bounds)
        yl = max(yl, min_bounds)
        yh = min(yh, max_bounds)
        zl = max(zl, min_bounds)
        zh = min(zh, max_bounds)

        for i in range(xl, xh+1):
            for j in range(yl, yh+1):
                for k in range(zl, zh+1):
                    if inst == 'on':
                        coordinates.add((i,j,k))
                    else:
                        if (i,j,k) in coordinates:
                            coordinates.remove((i,j,k))

    return len(coordinates)


def parse(l):
    status = []
    for line in l:
        c = []
        x,y = line.split()
        c.append(x)
        for element in y.split(','):
            start, stop = element.replace('x=', '').replace('y=', '').replace('z=', '').split('..')
            c.append((int(start), int(stop)))
        status.append(tuple(c))
    return status


def reactor_2(l):
    status = parse(l)
    return run(status)

def cubes_overlap(c1, c2):
    x_1, y_1, z_1 = c1
    x_2, y_2, z_2 = c2
    if x_1[1] < x_2[0] or x_2[1] < x_1[0] or z_1[1] < z_2[0] or z_2[1] < z_1[0] or y_1[1] < y_2[0] or y_2[1] < y_1[0]:
        return False

    return True

def helper(a, b):
    a_l, a_h = a
    b_l, b_h = b
    if b_l <= a_l and b_h >= a_h:
        return [a] #fine
    if b_h < a_l or b_l > a_h:
        return [a] #fine
    if b_l <= a_l and b_h < a_h:
        return [(a_l, b_h), (b_h+1, a_h)]
    if b_h >= a_h and b_l > a_l:
        return [(a_l, b_l-1), (b_l, a_h)]
    if b_l > a_l and b_h < a_h:
        return [(a_l, b_l-1), (b_l, b_h), (b_h+1, a_h)]

    raise Exception('Meh')


def cube_subtract(c1, c2):
    x_1, y_1, z_1 = c1
    x_2, y_2, z_2 = c2
    xs = helper(x_1, x_2)
    ys = helper(y_1, y_2)
    zs = helper(z_1, z_2)
    cubes = []
    for x in xs:
        for y in ys:
            for z in zs:
                if not cubes_overlap((x,y,z), c2):
                    cubes.append((x,y,z))
    return cubes

def run(status):
    regions = []
    for inst, x, y, z in status:
        next_regions = []
        cube_op = (x,y,z)
        if inst == 'on':
            on_cubes = [cube_op]
            for cube in regions:
                next_regions.append(cube)
                next_on_cubes = []
                for c in on_cubes:
                    if cubes_overlap(c, cube):
                        next_on_cubes.extend(cube_subtract(c, cube))
                    else:
                        next_on_cubes.append(c)
                on_cubes = next_on_cubes
            next_regions.extend(on_cubes)
        else:
            for cube in regions:
                if cubes_overlap(cube_op, cube):
                    next_regions.extend(cube_subtract(cube, cube_op))
                else:
                    next_regions.append(cube)
        regions = next_regions

    return size(regions)


def size(regions):
    total = 0
    for cube in regions:
        x,y,z = cube
        x_l, x_h = x
        y_l, y_h = y
        z_l, z_h = z
        vol = (1+x_h - x_l) * (1+y_h - y_l) * (1+z_h - z_l)
        total += vol

    return total