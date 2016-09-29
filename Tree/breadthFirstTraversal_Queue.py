from tree import *

def printBFS(root):
    if root == None:
        return
    Queue = list()
    Queue.append(root)
    while len(Queue) != 0:
        x = Queue.pop(0)
        if x == None:
            break
        print(x.data,end=' ')
        Queue.append(x.left)
        Queue.append(x.right)


"""  To print level by level
def printBFS(root):
    if root == None:
        return
    Queue = list()
    Queue.append(root)
    while 1:
        size = len(Queue)
        if size == 0:
            break
        while size != 0:
            x = Queue.pop(0)
            if x == None:
                break
            print(x.data,end=' ')
            Queue.append(x.left)
            Queue.append(x.right)
            size -= 1
        print()
"""
printBFS(root)
