from Tree_traversal.inorder import inorder_recursive
from Tree_traversal.preorder import preorder_recursive
from Tree_traversal.postorder import postorder_recursive
from Tree_traversal.levelorder import levelorder
class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right =None 

root = Node(10)
root.left=Node(11)
root.right=Node(11)
root.left.left = Node(12)
root.right.right = Node(12)

# traversing the tree
inorder_recursive(root)
print()
print(preorder_recursive(root))
print(postorder_recursive(root))
levelorder(root)
