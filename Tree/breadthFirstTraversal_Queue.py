# from tree import *

'''
#To print whole tree in one line
def printBFS(root):
    if root == None:
        return
    Queue = list()
    Queue.append(root)
    while len(Queue) != 0:
        x = Queue.pop(0)
        print(x.data,end=' ')
        if x.left is not None: Queue.append(x.left)
        if x.right is not None: Queue.append(x.right)
'''
# printBFS(root)

#  To print level by level
def printBFS(root):
    if root == None:
        return
    Queue = list()
    Queue.append(root)
    while 1:
        size = len(Queue)
        if size == 0:
            break
        while size > 0:
            x = Queue.pop(0)
            print(x.data,end=' ')
            if x.left != None: Queue.append(x.left)
            if x.right != None: Queue.append(x.right)
            size -= 1
        print()


