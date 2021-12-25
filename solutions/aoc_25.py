def cucumber_1(l):
    souths, easts, max_y, max_x = parse(l)
    count = 0
    while step(souths, easts, max_y, max_x):
        count += 1

    return count + 1

def step(souths, easts:set, max_y, max_x):

    easts_to_remove = set()
    easts_to_add = set()
    souths_to_add = set()
    souths_to_remove = set()
    for el in easts:
        x,y = el
        next_x = (x+1) % max_x
        if (next_x,y) in easts or (next_x,y) in souths:
            continue
        else:
            easts_to_remove.add(el)
            easts_to_add.add((next_x,y))
    easts.difference_update(easts_to_remove)
    easts.update(easts_to_add)
    for el in souths:
        x,y = el
        next_y = (y+1) % max_y
        if (x,next_y) in easts or (x,next_y) in souths:
            continue
        else:
            souths_to_remove.add(el)
            souths_to_add.add((x,next_y))
    souths.difference_update(souths_to_remove)
    souths.update(souths_to_add)

    return len(souths_to_remove) > 0 or len(easts_to_remove) > 0
    

def parse(l):
    souths = set()
    easts = set()
    for y in range(len(l)):
        for x in range(len(l[y])):
            if l[y][x] == '>':
                easts.add((x,y))
            elif l[y][x] == 'v':
                souths.add((x, y))
            else:
                pass
    return souths, easts, len(l), len(l[0])
