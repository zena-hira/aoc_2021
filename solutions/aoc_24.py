
def run_input(input):
    z = 0
    for ((a,b,c), w) in zip(abcs, input):
        z = step(a,b,c,int(w),z)
    return z == 0

def step(a,b,c,w,z):
    if ((z % 26) + b) != w:
        return ((z // a) * 26) + w + c
    else:
        return z // a

abcs = [  (1,10,2),
          (1,15,16),
          (1,14,9),
          (1,15,0),
          (26,-8,1),
          (1,10,12),
          (26,-16,6),
          (26,-4,6),
          (1,11,3),
          (26,-3,5),
          (1,12,9),
          (26,-7,3),
          (26,-15,2),
          (26,-7,3)
         ]

def search(mini=False):
    if mini:
        q = [(0, 0, i, []) for i in range(9,0, -1)]  #  z, index, w to try next, w's used
    else:
        q = [(0, 0, i, []) for i in range(0,10)]  #  z, index, w to try next, w's used

    seen = set()

    while len(q) > 0:
        z, i, w, used = q.pop()

        if (i,z,w) in seen:
            continue
        seen.add((i,z, w))

        if i > 10 and z >= 17576:
            continue

        a,b,c = abcs[i]
        z = step(a,b,c,w,z)
        if i+1 == 14:
            if z == 0:
              return used+[w]

        else:
            if mini:
                r = range(9,0, -1)
            else:
                r = range(0,10)

            for j in r:
                if (i+1, z, j) not in seen:
                    q.append((z, i+1, j, used+[w]))

def alu_1():
    # commands = parse(l)

    # print(run(commands, (int(x) for x in '98491959997994')))
    #
    # print(run(commands, (int(x) for x in '61191516111321')))

    return(search(mini=False))



def parse(l):
    commands = []
    for instr in l:
        op, arg1, *arg2 = instr.split(' ')
        if op == 'inp':
            commands.append([op, arg1])
        else:
            arg2 = arg2[0]
            if arg2 not in "wxyz":
                arg2 = int(arg2)
            commands.append([op, arg1, arg2])
    return commands

def charsIn(i):
    if i == 0:
        return ''
    else:
        return charsIn(i//26) + chr(65 + (i % 26))

def run(commands, input):
    memory = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    ops = { 'add': (lambda a, b: a + b),
            'mul': (lambda a, b: a * b),
            'div': (lambda a, b: a // b),
            'mod': (lambda a, b: a % b),
            'eql': (lambda a, b: int(a == b))
          }
    for (op, a1, *a2) in commands:
        if op == 'inp':
            memory[a1] = next(input)
        else:
            a2 = a2[0]

            v1 = memory[a1]
            if type(a2) is str:
                v2 = memory[a2]
            else:
                v2 = a2
            memory[a1] = ops[op](v1, v2)
    return memory

def alu_2():
    return(search(mini=True))