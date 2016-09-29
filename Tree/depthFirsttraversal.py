def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)

def preOrder(root):
    if root == None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")
