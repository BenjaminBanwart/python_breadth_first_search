from collections import deque

class Node:     # TreeNode
    def  __init__(self, key):
        if key == "null":
            self.data = None
        else:
            self.data = key
        self.left = None
        self.right = None

def max_levels(arr):
    levels = 0
    for i in range(10):
        if len(arr) == 2**i - 1:
            levels = i + 1
            break


    root = Node(arr[0])
    root.left = Node(arr[1])
    root.right = Node(arr[2])
    root.left.left = Node(arr[3])
    root.left.right = Node(arr[4])
    #root.right.left = Node(arr[5]) (we skip this to avoid problems)
    root.right.right = Node(arr[6])

    print(levelMax(root))

def levelMax(root):
    Q = deque()
    V = []
    M = set()
    bigs = []

    Q.appendleft(root)

    while len(Q) != 0:
        big = 0
        for _ in range(len(Q)):
            cur = Q.pop()
            V.append(cur)
            if cur.data > big:
                big = cur.data
            for child in [cur.left, cur.right]:
                if child not in M and child != None:
                    Q.appendleft(child)
                    M.add(child)
        bigs.append(big)
    return bigs

max_levels([5, 3, 8, 2, 4, 'null', 9])