
def increase(l):
    counter = 0
    for idx in range(0, len(l)):
        if int(l[idx-1]) < int(l[idx]):
            counter += 1
    return counter


def window_function(l):
    window = [l[0], l[1], l[2]]
    counter = 0
    c = sum(window)
    for idx in range(2, len(l)):
        window = window[1:]+[l[idx]]
        c2 = sum(window)
        if c2 > c:
            counter += 1
        c = c2
    return counter