#from tree import *
# from depthFirstTraversal import *

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def printSpiral(root):
    if root is None:
        return
    ltr = list()
    rtl = list()
    ltr.append(root)
    while len(ltr) !=0 or len(rtl) != 0:
        while len(ltr) != 0:
            x = ltr.pop()
            print(x.data,end=" ")
            if x.left: rtl.append(x.left)
            if x.right: rtl.append(x.right)

        while len(rtl) != 0:
            y = rtl.pop()
            print(y.data,end=" ")
            if y.left: ltr.append(y.right)
            if y.right: ltr.append(y.left)


root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

printSpiral(root)


### To change the direction of printing ###
"""
while len(ltr) !=0 or len(rtl) != 0:
        while len(ltr) != 0:
            x = ltr.pop()
            print(x.data,end=" ")
            if x.left: rtl.append(x.right)
            if x.right: rtl.append(x.left)

        while len(rtl) != 0:
            y = rtl.pop()
            print(y.data,end=" ")
            if y.left: ltr.append(y.left)
            if y.right: ltr.append(y.right)
"""
