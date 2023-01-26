class node:
    def __init__(self, dist, pos, arr, moves=[]):
        self.dist = dist
        self.pos = pos
        self.arr = arr
        self.h = pos + dist
        self.moves = moves
        self.next = [None * 4]

    def add(self, node):
        if node.h < self.h:
            f


class Tree:
    def __init__(self, root):
        self.root = root

    def add(self, node):
