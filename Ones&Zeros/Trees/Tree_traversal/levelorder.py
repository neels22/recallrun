from collections import deque

def levelorder(root):

    if not root:
        return 
    
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.value,end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        

