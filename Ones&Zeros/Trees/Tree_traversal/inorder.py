



# left, node, right

def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.value,end=" ")
        inorder_recursive(root.right)





