import heightOfTree
from depthFirstTraversal import *

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

root = Node(5)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(4)
root.left.right = Node(9)
root.right.left = Node(3)
root.right.right = Node(7)

# print("Height of the Tree is:",heightOfTree.height(root))
# print("In-Order Traversal: ")
# inOrder(root)
# print("\nPre-Order Traversal: ")
# preOrder(root)
# print("\nPost-Order Traversal: ")
# postOrder(root)
