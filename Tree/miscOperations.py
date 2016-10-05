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

def size(root):
    if root == None:
        return 0
    return(size(root.left) + 1 + size(root.right))

def countLeafNodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    return countLeafNodes(root.left) + countLeafNodes(root.right)

def height(root):
    if root == None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

def isHeightBalanced(root):
    if root is None:
        return True
    l = height(root.left)
    r = height(root.right)
    if abs(l-r) <= 1 and isHeightBalanced(root.left) and isHeightBalanced(root.right):
        return True
    return False

def findWidth(root):
    if root == None:
        return
    Queue = list()
    Queue.append(root)
    width = 0
    while 1:
        size = len(Queue)
        if size > width:
            width = size
        if size == 0:
            break
        while size != 0:
            x = Queue.pop(0)
            if x.left: Queue.append(x.left)
            if x.right: Queue.append(x.right)
            size -= 1
    return width

def doubleTree(root):
    if root is None:
        return
    doubleTree(root.left)
    doubleTree(root.right)
    temp = Node(root.data)
    temp.left = root.left
    root.left = temp

# printLeftView(root)
# printRightview(root)
# printTopView(root)
# print(size(root))
# print("No. of leafs: ",countLeafNodes(root))
# print("height of the tree is",height(root))
# print("Tree is height balanced") if isHeightBalanced(root) else print("Tree is not height balanced")
# print("Width of the tree is: ",findWidth(root))
# doubleTree(root)
