from collections import deque


def bfs(adj_list,startingnode):
    # bfs uses queue data structure
    # visited set to keep track of nodes that are already visited

    queue =deque()
    visited = set()

    queue.append(startingnode)
    visited.add(startingnode)


    while queue:
        node = queue.popleft()
        print(node)

        for adjnode in adj_list[node]:
            if adjnode not in visited:
                visited.add(adjnode)
                queue.append(adjnode)







    




