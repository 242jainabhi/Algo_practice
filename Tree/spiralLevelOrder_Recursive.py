from miscOperations import height

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def levelOrder(root):
    if root is None:
        return
    h = height(root)
    ltr = False
    for i in range(1,h+1):
        printSpiral(root,i,ltr)
        ltr = not ltr
        print()

def printSpiral(root, i, ltr):
    if root is None:
        return
    if i == 1:
        print(root.data,end=" ")
    elif i > 1:
        if ltr:
            printSpiral(root.left, i-1, ltr)
            printSpiral(root.right, i-1, ltr)
        else:
            printSpiral(root.right, i-1, ltr)
            printSpiral(root.left, i-1, ltr)


root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(14)
root.right.right.right = Node(15)

levelOrder(root)
