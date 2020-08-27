# By: Yusuf Ali
# This program Executes  a Level order Traversal
# It searches each level of nodes before going and searching the next level of nodes

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(3)
insert(r,Node(5))
insert(r, Node(9))
insert(r, Node(2))
insert(r, Node(4))
insert(r, Node(0))
insert(r, Node(2))
inorder(r)