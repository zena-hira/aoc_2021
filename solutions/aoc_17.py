import math
import re

def shot_1(l):
    target = parse(l)
    #print(target)
    maxy = 0
    for sx in range(0,1000):
        for sy in range(-100, 1000):
            r = trace((sx,sy), target)
            if r is not False:
                #print (sx, sy, r)
                maxy = max(r, maxy)
    return maxy

def trace(v, target):

    p = (0,0)
    tr = [(p,v)]
    xlo, xhi, ylo, yhi = target
    maxy = 0
    while True:
        np, nv = step(p, v)
        tr.append((np,nv))
        #print (np, nv)
        nx,ny = np
        maxy = max(maxy, ny)
        if nx >= xlo and nx <= xhi and ny >= ylo and ny <= yhi:
            #print(tr)
            return maxy # hit the target
        if nx > xhi or ny < ylo:
            return False # went too far
        p = np
        v = nv

def step(p, v):
    x,y = p
    vx,vy = v
    dvx = 0 if vx == 0 else -int(math.copysign(1, vx))
    return (x+vx, y+vy), (vx + dvx, vy - 1)

def shot_2(l):
    target = parse(l)
    xlo, xhi, ylo, yhi = target
    c = 0
    for sx in range(0,xhi+1):
        for sy in range(ylo-1, 1000):
            r = trace((sx,sy), target)
            if r is not False:
                c += 1
    return c

def parse(l):
    # target area: x=96..125, y=-144..-98
    m = re.match(r"target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)", l[0])
    xlo, xhi, ylo, yhi = map(int,[m.group(1), m.group(2), m.group(3), m.group(4)])
    return xlo, xhi, ylo, yhi