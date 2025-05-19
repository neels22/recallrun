


# adj list uses dictionary where each key is a node and value is a list of nodes
# for undirected graph the edge is added in both directions that means both the nodes (keys) will have the other node in their respective lists
# for directed graph the edge is added in one direction that means only one of the nodes (key) will have the other node in its list

# graph will have functions to create empty graph , add node,  add edges to each node, display graph 

class Graph:
    def __init__(self):
        """Initialize the graph with an empty adjacency list. whenever we create a graph object we will create an empty dictionary"""
        self.adj_list = {}

    def add_node(self, node):
        """add a node to the graph. if the node is already present in the graph then it will not be added again"""
        if node not in self.adj_list:
            self.adj_list[node] = [] # create an empty list for the node
        else:
            print(f"Node {node} already exists in the graph. Not adding again.")

    def add_edge(self, node1, node2):
        """adding edge between the 2 nodes, if any of the node not present in the graph it will call the add_node function to add the node to the graph"""
        """after adding the node it will check if the edge is already present in the graph or not, if it is present then it will not add the edge again"""
        if node1 not in self.adj_list:
            self.add_node(node1)
        if node2 not in self.adj_list:
            self.add_node(node2)
        
        # add the edge in both directions for undirected graph if the edge is not already present in that direction
        if node2 not in self.adj_list[node1]:
            self.adj_list[node1].append(node2)
        if node1 not in self.adj_list[node2]:
            self.adj_list[node2].append(node1)

    def display_graph(self):
        """display the graph in adjacency list format"""
        for node in self.adj_list:
            # print("node ",node, "-> ", self.adj_list[node])

            for adjnode in self.adj_list[node]:
                print(f"{node} -> {adjnode}")


    
            


if __name__ == "__main__":

    graphobject = Graph()
    graphobject.add_node(1)
    graphobject.add_node(2)
    graphobject.add_node(3)

    graphobject.add_edge(1, 2)
    graphobject.add_edge(1, 3)
    graphobject.add_edge(2, 3)

    graphobject.display_graph()
    print(graphobject.adj_list)






        





