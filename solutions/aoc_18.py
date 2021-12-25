import ast
import copy
import itertools


def snailfish_1(l):
    x = []
    for line in l:
        x.append(ast.literal_eval(line))

    current = x[0]
    for n in x[1:]:
        current = reduce_as_far_as_possible([current, n])

    #print(current)
    mag = magnitude(current)
    return mag

def magnitude(sn):
    if type(sn) is int:
        return sn

    a,b = sn
    ma = magnitude(a)
    mb = magnitude(b)
    return (3*ma) + (2*mb)

def reduce_as_far_as_possible(sn):
    current = sn
    #print(current)

    next = step(current)
    while next is not None:
        #print(current)
        current = next
        next = step(current)
    return current

def step(sn):
    next, modified, _ = do_step(sn, 0, 0, False, sn)
    if modified:
        return next
    next, modified, _ = do_step(sn, 0, 0, True, sn)
    if modified:
        return next
    return None

def do_step(sn, depth, next_idx, do_split, root):

    if depth >= 4 and type(sn) is list:
        a,b = sn
        #print('explode')
        #print(' ==>' + str(['sn', sn, 'd', depth, 'i', next_idx]))
        modify(root, 0, next_idx - 1, lambda x: x + a)
        modify(root, 0, next_idx + 2, lambda x: x + b)
        return 0, True, None

    if type(sn) is int:
        if sn >= 10 and do_split:
            #print('split')
            #print(' ==>' + str(['sn', sn, 'd', depth, 'i', next_idx]))
            return [int(sn / 2), int((sn+1) / 2)], True, None
        return sn, False, next_idx+1

    a,b = sn
    ra, changed, next_idx1 = do_step(a, depth+1, next_idx, do_split, root)
    if changed:
        sn[0] = ra
        return sn, True, None

    rb, changed, next_idx2 = do_step(b, depth+1, next_idx1, do_split, root)
    if changed:
        sn[1] = rb
        return sn, True, None

    return sn, False, next_idx2

def modify(sn, nextIdx, targetI, fn):
    if targetI < 0:
        return sn

    if type(sn) is list:
        a,b = sn
        ra, changed, nextIdx1 = modify(a, nextIdx, targetI, fn)
        if changed:
            sn[0] = ra
            return sn, True, None

        rb, changed, nextIdx2 = modify(b, nextIdx1, targetI, fn)
        if changed:
            sn[1] = rb
            return sn, True, None

        return sn, False, nextIdx2

    if type(sn) is int:
        if targetI == nextIdx:
            return fn(sn), True, None
        return sn, False, nextIdx+1


def snailfish_2(l):
    x = []
    for line in l:
        x.append(ast.literal_eval(line))

    mag = 0
    for (a,b) in itertools.combinations(x, 2):
        mag = max(mag, magnitude(reduce_as_far_as_possible(copy.deepcopy([a,b]))))
        mag = max(mag, magnitude(reduce_as_far_as_possible(copy.deepcopy([b,a]))))

    return mag

#-----Solution 2--------#


class Node(object):
    def __init__(self, value=None, left = None, right = None, parent = None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def to_list(self):
        if self.value is None:
            return [self.left.to_list(), self.right.to_list()]

        return self.value

    def magnitude(self):
            if self.value is None:
                return (3*self.left.magnitude()) + (2*self.right.magnitude())
            else:
                return self.value

def snailfish_solution_2_1(l):
    x = []

    for line in l:
        x.append(make_tree(ast.literal_eval(line), None))

    current = x[0]
    for next in x[1:]:
        tree = Node(left=current, right=next, parent=None)
        current.parent = tree
        next.parent = tree
        traverse_explode(tree, 0)
        b = traverse_split(tree)
        while b:
            traverse_explode(tree, 0)
            b = traverse_split(tree)
        current = tree

    return current.magnitude()

def add_left_sibling(p, value):
    parent = p.parent
    current = p
    if parent is None:
        return
    while current is parent.left:
        parent = parent.parent
        if parent is None:
            return
        current = current.parent

    current = parent.left
    while current.right is not None:
        current = current.right

    current.value += value
    return

def add_right_sibling(p, value):
    parent = p.parent
    current = p
    if parent is None:
        return
    while current is parent.right:
        parent = parent.parent
        if parent is None:
            return
        current = current.parent

    current = parent.right
    while current.left is not None:
        current = current.left

    current.value += value
    return

def traverse_explode(tree, depth):

    if tree.value is None and depth != 4:
        x = traverse_explode(tree.left, depth + 1)
        y = traverse_explode(tree.right, depth + 1)
        return (x or y)

    elif tree.value is None and depth == 4:
        add_left_sibling(tree, tree.left.value)
        add_right_sibling(tree, tree.right.value)
        tree.value = 0
        tree.left = None
        tree.right = None
        return True

    return False

def traverse_split(tree):

    if tree.value is not None and tree.value >= 10:
        tree.left = Node(int(tree.value / 2), parent=tree)
        tree.right = Node(int((tree.value+1) / 2), parent=tree)
        tree.value = None
        return True

    elif tree.value is None:
        if traverse_split(tree.left):
            return True
        else:
            return traverse_split(tree.right)

    return False

def make_tree(x, p):

    if type(x) is int:
        tree = Node(x, parent = p)
        return tree

    if type(x) is list:
        tree = Node(parent = p)
        tree.left = make_tree(x[0], tree)
        tree.right = make_tree(x[1],tree)
        return tree


def combine_trees(t1, t2):

    tree = Node(left=t1, right=t2, parent=None)
    t1.parent = tree
    t2.parent = tree
    traverse_explode(tree, 0)
    b = traverse_split(tree)
    while b:
        traverse_explode(tree, 0)
        b = traverse_split(tree)
    return tree

def snailfish_solution_2_2(l):
    x = []

    for line in l:
        x.append(ast.literal_eval(line))

    mag = 0
    for (a,b) in itertools.combinations(x, 2):
        mag = max(mag, combine_trees(make_tree(a, None), make_tree(b, None)).magnitude())
        mag = max(mag, combine_trees(make_tree(b, None), make_tree(a, None)).magnitude())

    return mag