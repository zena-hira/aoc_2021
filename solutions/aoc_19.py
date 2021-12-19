import itertools
from collections import defaultdict
from math import copysign


class Scanner(object):
    def __init__(self, id, beacons):
        self.id = id
        self.beacons = beacons
        distances, per_beacon = calculate_distance_matrix(beacons)
        self.distance = distances
        self.per_beacon = per_beacon
        self.beacons_as_set = frozenset(beacons)

def star_1(l):
    scanners = { id: Scanner(id, beacons) for (id, beacons) in parse(l).items() }
    mappings = {}

    skeys = sorted(list(scanners.keys()))
    for i in range(0, len(skeys)):
        for j in range(i+1, len(skeys)):
            r = align(scanners[i], scanners[j])
            if r is not None:
                mappings[(i,j)] = r
                mappings[(j,i)] = align(scanners[j], scanners[i]) #couldnt figure that out

    all_beacons = set()
    remapped_beacons_per_scanner = {}

    # walk i's beacons back to scanner 0
    for i in skeys:
        transes = path_to_zero(i, mappings)
        is_remapped = []
        remapped_beacons_per_scanner[i] = is_remapped
        for b in scanners[i].beacons:
            for ori,dist in transes:
                b = apply_orientation_dist(b, ori, dist)
            all_beacons.add(b)
            is_remapped.append(b)


    return len(all_beacons)

def path_to_zero(s, mappings):
    to_try = [(s, [])]
    visited = set()
    while(True):
        x, mapping = to_try.pop()
        if x == 0:
            return mapping
        if x in visited:
            continue
        visited.add(x)
        for k, mp in mappings.items():
            a,b = k
            if b != x or a in visited:
                continue
            to_try.append((a, mapping+[mp]))



# given 2 scanners, returns scanner2's position, and the orientation adjustment relative to scanner1 if they are aligned
#   or None if no mapping can be found
def align(scanner1, scanner2):
    s1_dists = set(scanner1.per_beacon.keys())
    s2_dists = set(scanner2.per_beacon.keys())
    possible_dists = s1_dists.intersection(s2_dists)

    attempted = set()

    for pd in possible_dists:
        for (p1i, p2i) in scanner1.per_beacon[pd]:
            p1 = scanner1.beacons[p1i]
            p2 = scanner1.beacons[p2i]

            for (q1i, q2i) in scanner2.per_beacon[pd]:
                q1 = scanner2.beacons[q1i]
                q2 = scanner2.beacons[q2i]
                for possible in itertools.chain(match2(p1,p2,q1,q2), match2(p1,p2,q2,q1)):
                    if possible in attempted:
                        continue
                    attempted.add(possible)
                    if find_12(possible, scanner1, scanner2):
                        return possible


def find_12(possible, scanner1, scanner2):
    ori, dis = possible
    s2bs = set(apply_orientation_dist(p, ori, dis) for p in scanner2.beacons)
    return len(scanner1.beacons_as_set.intersection(s2bs)) >= 12

# applies all orientations and checks if the distances are still the same
def match2(p1, p2, q1, q2):
    for orientation in all_orientation_modifiers():
        q1r = remap(q1, orientation)
        dist = calc_dist_array(p1, q1r)

        q2r = apply_orientation_dist(q2, orientation, dist)
        if q2r == p2:
            yield orientation, dist

def apply_orientation_dist(p, orientation, dist):
    x1,y1,z1 = dist
    x2,y2,z2 = remap(p, orientation)
    return (x1+x2, y1+y2, z1+z2)

def identity():
    return (1,2,3), (0,0,0)

def remap(p, orientation):
    return tuple(int(copysign(1,i)) * p[abs(i)-1] for i in orientation)

def calc_dist_array(p1, p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return (x1-x2, y1-y2, z1-z2)

def all_orientation_modifiers():
    res = set()
    for ps in itertools.permutations([1,2,3]):
        for t in itertools.product(*((x, -x) for x in ps)):
            res.add(tuple(t))
    return res

def calculate_distance_matrix(beacons):
    distances = { }
    per_beacon = defaultdict(list)
    for i in range(0, len(beacons)):
        for j in range(i+1, len(beacons)):
            x1,y1,z1 = beacons[i]
            x2,y2,z2 = beacons[j]
            distance = (((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2))
            distances[(i,j)] = distance
            per_beacon[distance].append((i,j))

    return distances, per_beacon

def parse(l):
    scanners = {}
    scanner = []
    for line in l:
        if line == '':
            continue
        parts = line.split(' ')
        if len(parts) == 4:
            s = int(parts[2])
            scanner = []
            scanners[s] = scanner
            continue

        x,y,z = line.split(',')
        scanner.append( (int(x), int(y), int(z)) )

    return scanners


def star_2(l):
    x = sorted(list(all_orientation_modifiers()))
    scanners = {id: Scanner(id, beacons) for (id, beacons) in parse(l).items()}
    mappings = {}

    skeys = sorted(list(scanners.keys()))
    for i in range(0, len(skeys)):
        for j in range(i + 1, len(skeys)):
            r = align(scanners[i], scanners[j])
            if r is not None:
                mappings[(i, j)] = r
                mappings[(j, i)] = align(scanners[j], scanners[i])

    all_beacons = set()
    remapped_beacons_per_scanner = {}

    # walk (0,0,0) back to scanner 0
    for i in skeys:
        transes = path_to_zero(i, mappings)
        is_remapped = []
        remapped_beacons_per_scanner[i] = is_remapped
        b = (0,0,0)
        for ori, dist in transes:
            b = apply_orientation_dist(b, ori, dist)
        all_beacons.add(b)

    max_man = 0
    for (a,b,c) in all_beacons:
        for (d,e,f) in all_beacons:
            max_man = max(abs(a-d)+abs(b-e)+abs(c-f), max_man)

    return max_man
