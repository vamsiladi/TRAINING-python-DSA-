class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key)+"->",end='')
        inorder(root.right)
def insert(node, key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node

def minValueNode(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current
def deleteNode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left=deleteNode(root.left,key)
    elif (key>root.key):
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp


root=None
root=insert(root, 8)
root=insert(root, 3)
root=insert(root, 1)
root=insert(root, 6)
root=insert(root, 7)
root=insert(root, 10)
root=insert(root, 14)
root=insert(root, 4)
print("Inorder traversal",end='')
inorder(root)
