from depthFirstTraversal import *
from tree import *

def printLeftView(root):
    if root == None:
        return
    print(root.data,end=" ")
    printLeftView(root.left)

def printRightview(root):
    if root == None:
        return
    print(root.data,end=" ")
    printRightview(root.right)


def printLeftToRight(root):
    if root == None:
        return
    printLeftToRight(root.left)
    print(root.data,end=" ")

def printTopView(root):
    if root == None:
        return
    printLeftToRight(root.left)
    printRightview(root)

# printLeftView(root)
# printRightview(root)
# printTopView(root)
