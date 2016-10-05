from tree import *

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def childrenSum(root):
    left = 0
    right = 0
    if root is None or root.left is None and root.right is None:
        return 1
    else:
        if root.left is not None:
            left = root.left.data
        if root.right is not None:
            right = root.right.data
        if root.data == left+right and childrenSum(root.left) and childrenSum(root.right):
            return 1
        else:
            return 0


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

print(childrenSum(root))
