from tree import *
from breadthFirstTraversal_Queue import *

def mirrorTree(root):
    if root == None:
        return
    mirrorTree(root.left)
    mirrorTree(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp

printBFS(root)
mirrorTree(root)
print()
printBFS(root)
