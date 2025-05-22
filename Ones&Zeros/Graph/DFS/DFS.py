
def dfs_recursive(adj_list, startingnode, visited=None):
    if visited is None:
        visited = set()

    visited.add(startingnode)
    print(startingnode)

    for adjnode in adj_list[startingnode]:
        if adjnode not in visited:
            dfs_recursive(adj_list, adjnode, visited)




def dfs_iterative(adj_list,startingnode):
    # dfs uses stack data structure
    # visited set to keep track of nodes that are already visited
    stack = []
    visited = set()

    stack.append(startingnode)
    visited.add(startingnode)

    while stack:
        node = stack.pop()
        print(node)

        for adjnode in adj_list[node]:
            if adjnode not in visited:
                visited.add(adjnode)
                stack.append(adjnode)
            


