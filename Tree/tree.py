from breadthFirstTraversal_Queue import printBFS

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def doubleTree(root):
    if root is None:
        return
    doubleTree(root.left)
    doubleTree(root.right)
    temp = Node(root.data)
    temp.left = root.left
    root.left = temp

root = Node(5)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(4)
root.left.right = Node(9)
root.right.left = Node(3)
root.right.right = Node(7)

printBFS(root)
doubleTree(root)
print("After Doubling the Tree:")
printBFS(root)
