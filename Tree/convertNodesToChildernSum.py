#from tree import *
from depthFirstTraversal import *

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def increment(root,diff):
    if root.left is not None:
        root.left.data += diff
        increment(root.left,diff)
    elif root.right is not None:
        root.right.data += diff
        increment(root.right,diff)

def convertTree(root):
    left = 0
    right = 0
    if root is None or root.left is None and root.right is None:
        return 1
    else:
        convertTree(root.left)
        convertTree(root.right)

        if root.left is not None:
            left = root.left.data
        if root.right is not None:
            right = root.right.data
        diff = left+right - root.data

        if diff > 0:
            root.data += diff
        if diff < 0:
            increment(root,-diff)



root = Node(50)
root.left = Node(7)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(30)

inOrder(root)
convertTree(root)
print()
inOrder(root)
