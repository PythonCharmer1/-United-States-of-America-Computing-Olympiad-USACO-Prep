# Python 3.7
# This Program tells the diameter from one Node of the tree to another
# By Yusuf Ali



# Finds the Height of the tree
class TreeHeight:
    def __init(self):
        self.h = 0

# Creates the Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# This Function find the diameter for the binary tree
def diameter(root, height):
    lh = TreeHeight()
    rh = TreeHeight()
    if root is None:
        height.h = 0
        return 0
    ldiameter = diameter(root.left, lh)
    rdiameter = diameter(root.right, rh)
    height.h = max(lh.h, rh.h) + 1
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))

#Creates all of the nodes
root = Node(0)
root.left = Node(50)
root.right = Node(100)
root.left.left = Node(200)
root.left.right = Node(500)


# Checks the root
def check(root):
    if root == None:
        return "Invalid Root"
check(root)

# Prints the diameter
height = TreeHeight()
print(diameter(root, height))

