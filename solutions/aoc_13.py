import re


def origami_1(l):
    dots,instructions = parse(l)
    #print(dots)
    #print(instructions)
    d2 = do_fold(dots, instructions[0])
    return len(d2)


def do_fold(dots, instruction):
    axis, z = instruction
    next = set()
    for (a,b) in dots:
        if (axis == "x"):
            if a < z:
                next.add((a,b))
            else:
                next.add((z - (a - z) , b))

        else: #y axis
            if b < z:
                next.add((a,b))
            else:
                next.add((a, z - (b - z)))
    return next


def parse(l):
    dots = set()
    for line in l:
        if line == '':
            break
        a,b = line.split(',')
        dots.add((int(a),int(b)))

    instructions = []
    for line in l:
        m = re.match(r"fold along (.)=([0-9]+)", line)
        if m:
            instructions.append((m.group(1), int(m.group(2))))

    return dots, instructions


def origami_2(l):
    dots, instructions = parse(l)
    for instruction in instructions:
        dots = do_fold(dots, instruction)

    xmax = max([a for a,b in dots]) + 1
    ymax = max([b for a,b in dots]) + 1

    for j in range(0, ymax):
        for i in range(0, xmax):
            if (i,j) in dots:
                print('#', end='')
            else:
                print(' ', end='')
        print('')

    return '^^^'