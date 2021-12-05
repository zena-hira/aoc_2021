
def submarine(l):
    horizontal, depth = 0, 0
    for element in l:
        command, distance = element.split()
        if command == 'forward':
            horizontal += int(distance)
        elif command == 'up':
            depth -= int(distance)
        else:
            depth += int(distance)

    return horizontal * depth


def submarine_with_aim(l):
    horizontal, depth, aim = 0, 0, 0
    for element in l:
        command, distance = element.split()
        distance = int(distance)

        if command == 'forward':
            horizontal += distance
            depth += (aim * distance)
        elif command == 'up':
            aim -= distance
        else: # down
            aim += distance

    return horizontal * depth
