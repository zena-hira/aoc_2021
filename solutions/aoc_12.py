from collections import defaultdict


def paths_1(l):
    graph = parse(l)
    q = [('start', set([]))] # next node, small caves seen so far

    total_count = 0
    while len(q) > 0:
        cNode, visited = q.pop()
        if cNode == 'end':
            total_count += 1
            continue

        if cNode in visited:
            continue
        # if upper dont put in visited
        if cNode.isupper():
            nextVisited = visited
        else:
            nextVisited = set(visited)
            nextVisited.add(cNode)

        nexts = graph[cNode]

        q.extend([(next, nextVisited) for next in nexts])

    return total_count


def parse(l):
    edges = defaultdict(set)
    for line in l:
        pre,post = line.split("-")
        edges[pre].add(post)
        edges[post].add(pre)
    return edges

def paths_2(l):
    graph = parse(l)

    used_paths = set([])
    # for every small cave set it as the one that can be visited twice
    for dupl in (key for key in graph.keys() if key.islower()):
        if dupl in ['start', 'end']:
            continue

        # next node, small caves, is it used twice, route
        q = [('start', set([]), False, [])]

        while len(q) > 0:
            cNode, visited, duplUsed, path = q.pop()
            if cNode == 'end':
                used_paths.add('-'.join(path))
                continue
            # seen more than twice or visited again and is not the dupUsed
            if (cNode == dupl and duplUsed) or (cNode in visited and (cNode != dupl)):
                continue

            if cNode.isupper():
                nextVisited = visited
                nextDupl = duplUsed
            else:
                nextVisited = set(visited)
                nextVisited.add(cNode)
                nextDupl = duplUsed or (cNode == dupl and cNode in visited)

            nexts = graph[cNode]
            q.extend([(next, nextVisited, nextDupl, ([cNode] + path)) for next in nexts])

    return len(used_paths)