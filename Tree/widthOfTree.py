class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

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
            if x == None:
                break
            if x.left: Queue.append(x.left)
            if x.right: Queue.append(x.right)
            size -= 1
    return width



root = Node(5)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(4)
root.left.right = Node(9)
root.right.left = Node(3)
root.right.right = Node(7)
root.right.right.left = Node(17)
root.right.right.left.right = Node(170)
print("Width of the tree is: ",findWidth(root))
