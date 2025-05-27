


def postorder_recursive(node):
    if node is None:
        return []
    return postorder_recursive(node.left) + postorder_recursive(node.right) + [node.value]