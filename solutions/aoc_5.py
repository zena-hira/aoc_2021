import math


def vents_1(l):

    lines = [ line for line in parse(l) if line['x1'] == line['x2'] or line['y1'] == line['y2'] ]
    coords = {}

    for line in lines:
        # for every x y add or increase dict entry
        for x in range(min(line['x1'], line['x2']), max(line['x1'], line['x2'])+1 ):
            for y in range(min(line['y1'], line['y2']), max(line['y1'], line['y2']) + 1):
                count = coords.get( (x,y), 0)
                coords[(x,y)] = count + 1

    res = len([c for c in coords.values() if c > 1 ])
    return res

def parse(l):
    lines = []

    for line_desc in l:
        pre, post = line_desc.split(' -> ')
        x1, y1 = map(int, pre.split(','))
        x2, y2 = map(int, post.split(','))
        lines.append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})
    return lines

def vents_2(l):

    lines = parse(l) # [ line for line in parse(l) if line['x1'] == line['x2'] or line['y1'] == line['y2'] ]
    coords = {}

    for line in lines:
        # verticals
        if line['x1'] == line['x2']:
            x = line['x1']
            for y in range(min(line['y1'], line['y2']), max(line['y1'], line['y2'])+1):
                count = coords.get( (x,y), 0)
                coords[(x,y)] = count + 1
        # horizontals
        elif line['y1'] == line['y2']:
            y = line['y1']
            for x in range(min(line['x1'], line['x2']), max(line['x1'], line['x2'])+1):
                count = coords.get( (x,y), 0)
                coords[(x,y)] = count + 1

        else:
            # diagonals
            xChange = int(math.copysign(1, line['x2'] - line['x1']))
            xCoords = range(line['x1'], line['x2'] + xChange, xChange)

            yChange = int(math.copysign(1, line['y2'] - line['y1']))
            yCoords = range(line['y1'], line['y2'] + yChange, yChange)

            for x, y in zip(xCoords, yCoords):
                count = coords.get( (x,y), 0)
                coords[(x,y)] = count + 1

    res = len([c for c in coords.values() if c > 1 ])
    return res
