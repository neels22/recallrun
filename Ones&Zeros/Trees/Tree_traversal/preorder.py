


def preorder_recursive(node):
    if node is None:
        return []
    return [node.value] + preorder_recursive(node.left) + preorder_recursive(node.right)