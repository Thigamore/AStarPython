# Thomas Lascaud
# 1/22/23
# A program to solve an 8 puzzle
# Please excuse the formatting, something weird is happening with the formatter

# from linkedList import node, LinkedList     || from original multiple file program

# Nodes for the queue
class node:
    # intializer
    def __init__(self, pos, arr, moves=[]):
        self.pos = pos
        self.arr = arr
        self.next = None
        self.prev = None
        self.moves = moves

    # returns a string version of the node
    def __str__(self):
        return f"pos: {self.pos}, arr: {self.arr}"

# A priority Queue
class PriorityQueue:
    # initializer
    def __init__(self, head):
        self.head = head

    # adds a node to the queu
    def add(self, node):
        current = self.head
        # if there is nothing in the queue, make it the head
        if current == None:
            self.head = node
        # adds node where it is smaller than the next one and bigger than the previous one, like a priority queue
        if node.pos <= current.pos:
            node.next = current
            current.prev = node
            self.head = node
            return
        # continues until it finds where to put the node
        while current.next != None:
            if node.pos <= current.next.pos:
                node.next = current.next
                current.next.prev = node
                current.next = node
                return
            current = current.next
        current.next = node
        node.prev = current

    #pops front node
    def pop(self):
        temp = self.head
        self.head = self.head.next
        return temp

    # returns a string version of the queue
    def __str__(self):
        if self.head != None:
            string = ""
            cur = self.head
            while cur.next != None:
                string += cur.__str__() + " | "
                cur = cur.next
            string += f"{cur.__str__()}"
            return string

# Finds manhantan distance for a square array of nxn dimensions
def manDist(arr):
    width = len(arr)
    dist = 0
    # math to find where man dist for each position when 0 is top left
    for i in range(width):
        for j in range(width):
            dist += abs(i - (arr[i][j] // width)) + \
                abs(j - (arr[i][j] % width))
    # does the same thing as above, but when 0 is in bottom right, please excuse the spaghetti
    (x, y) = findBlank(arr)
    arr[y][x] = width**2
    sub1(arr)
    dist2 = 0
    for i in range(width):
        for j in range(width):
            dist2 += abs(i - (arr[i][j] // width)) + \
                abs(j - (arr[i][j] % width))
    add1(arr)
    arr[y][x] = 0

    # returns smallest distance
    if dist < dist2:
        return dist
    else:
        return dist2

# subtracts 1 from each member of the array 
def sub1(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] -= 1

# adds 1 from each member of the array
def add1(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] += 1

# Swaps pos 1 and pos 2 in array, formatting isn't working so well for some reason
def swap(arr, pos1, pos2):
    arr[pos1[1]][pos1[0]], arr[pos2[1]][pos2[0]
                                        ] = arr[pos2[1]][pos2[0]], arr[pos1[1]][pos1[0]]

# Deep Copies array
def copy(arr):
    temp = [None] * len(arr)
    for i in range(len(arr)):
        temp[i] = arr[i].copy()
    return temp

# If number of inversions is odd, doesn't have a solution
def isPossible(arr):
    inv = 0
    for i in range(1, len(arr)):
        if arr[i] == 0:
            continue
        if arr[i-1] > arr[i]:
            inv += 1
    if inv % 2 == 1:
        return False
    return True

# Returns (x,y) pos of blank
def findBlank(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                return (j, i)


# finds the solution to the 8 puzzle
def findSolution(arr):
    # check if 8 puzzle is possible
    if not isPossible(arr):
        return -1
    # find basic info about arr
    width = len(arr)
    dist = manDist(arr)
    # create queue
    queue = PriorityQueue(node(dist, arr))
    # set basic variables
    prev = [arr]
    moves = 0
    pos = 0
    moves = []
    # while you haven't reached the goal state yet
    while dist != 0:
        # find where the blank is
        (x, y) = findBlank(arr)
        # checks all 4 possible moves to see if they are possible, then adds to priority queue
        if x - 1 >= 0:
            # get man dist after move
            tempArr = copy(arr)
            swap(tempArr, (x, y), (x-1, y))
            tempDist = manDist(tempArr)
            # check is the state of the 8 puzzle has already been seen
            if tempArr not in prev:
                # add to priority queue
                tempMoves = moves.copy()
                tempMoves.append("left")
                queue.add(node(tempDist + pos+1, tempArr, tempMoves))
                prev.append(tempArr)
        if x + 1 < width:
            # get man dist after move
            tempArr = copy(arr)
            swap(tempArr, (x, y), (x+1, y))
            tempDist = manDist(tempArr)
            # check is the state of the 8 puzzle has already been seen
            if tempArr not in prev:
                # add to priority queue
                tempMoves = moves.copy()
                tempMoves.append("right")
                queue.add(node(tempDist + pos+1, tempArr, tempMoves))
                prev.append(tempArr)
        if y - 1 >= 0:
            # get man dist after move
            tempArr = copy(arr)
            swap(tempArr, (x, y), (x, y-1))
            tempDist = manDist(tempArr)
            # check is the state of the 8 puzzle has already been seen
            if tempArr not in prev:
                # add to priority queue
                tempMoves = moves.copy()
                tempMoves.append("up")
                queue.add(node(tempDist + pos+1, tempArr, tempMoves))
                prev.append(tempArr)
        if y + 1 < width:
            # get man dist after move
            tempArr = copy(arr)
            swap(tempArr, (x, y), (x, y+1))
            tempDist = manDist(tempArr)
            # check is the state of the 8 puzzle has already been seen
            if tempArr not in prev:
                # add to priority queue
                tempMoves = moves.copy()
                tempMoves.append("down")
                queue.add(node(tempDist + pos+1, tempArr, tempMoves))
                prev.append(tempArr)
        # choose the next move as the one with lowest manDist + moves done
        tempNode = queue.pop()
        # get the information of the new node 
        arr = tempNode.arr
        dist = manDist(arr)
        pos = tempNode.pos - dist
        moves = tempNode.moves
    # return all the moves
    return moves


# gets the array from the user
def getArr():
    arr = []
    for i in range(3):
        tempArr = []
        for j in range(3):
            usrIn = int(input(f"Enter Tile on column {j} and row {i}: "))
            tempArr.append(usrIn)
        arr.append(tempArr)
    return arr

# prints the 8 puzzle
def print8Puz(arr):
    string = " "
    for row in arr:
        for num in row:
            string += str(num) + " "
        string += "\n "
    print(string)


# where the program runs

# get the array and then solve it
arr = getArr()
print8Puz(arr)
moves = findSolution(arr)
# print solved moves
print(f"{len(moves)} | {moves}")
