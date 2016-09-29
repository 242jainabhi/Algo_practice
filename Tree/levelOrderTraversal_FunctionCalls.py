from tree import *
from heightOfTree import *

# print(height(root))
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
            printGivenLevel(root,i)

def printGivenLevel(root,i):
    if root == None:
        return
    if i == 1:
        print(root.data)
    elif i > 1:
        printGivenLevel(root.left,i-1)
        printGivenLevel(root.right,i-1)

printLevelOrder(root)
