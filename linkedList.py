class node:
    def __init__(self, pos, arr, moves=[]):
        self.pos = pos
        self.arr = arr
        self.next = None
        self.prev = None
        self.moves = moves

    def __str__(self):
        return f"pos: {self.pos}, arr: {self.arr}"


class LinkedList:
    def __init__(self, head):
        self.head = head

    def add(self, node):
        current = self.head
        if current == None:
            self.head = node
        if node.pos <= current.pos:
            node.next = current
            current.prev = node
            self.head = node
            return
        while current.next != None:
            if node.pos <= current.next.pos:
                node.next = current.next
                current.next.prev = node
                current.next = node
                return
            current = current.next
        current.next = node
        node.prev = current

    def pop(self):
        temp = self.head
        self.head = self.head.next
        return temp

    def __str__(self):
        if self.head != None:
            string = ""
            cur = self.head
            while cur.next != None:
                string += cur.__str__() + " | "
                cur = cur.next
            string += f"{cur.__str__()}"
            return string
