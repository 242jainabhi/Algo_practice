class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
# sumList = []
def rootToLeafPaths(root,queue):
    if root == None:
        return
    queue.append(root)
    if root.left == None and root.right == None:
        for i in queue:
            print(i.data,end=' ')
        # x = sum([i.data for i in queue])
        # sumList.append(x)
        queue.pop()
        print()
    else:
        rootToLeafPaths(root.left,queue)
        rootToLeafPaths(root.right,queue)
        queue.pop()



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(16)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.left.left.right = Node(17)
root.left.right.left = Node(18)
root.left.right.right = Node(8)
# root.right.right.left = Node(9)
# root.right.right.right = Node(19)
root.left.left.right.left = Node(170)
root.left.left.right.left.right = Node(190)
root.left.right.left.right = Node(180)

queue = list()
print("Root to Leaf paths are: ")
rootToLeafPaths(root,queue)
    # sumList
