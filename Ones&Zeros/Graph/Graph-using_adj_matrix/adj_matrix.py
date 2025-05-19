



# An Adjacency Matrix is a 2D array where:

# Rows and columns represent vertices.

# The value at matrix[i][j] indicates whether there is an edge from vertex i to vertex j.

# For unweighted graphs: 1 (or True) means an edge exists, 0 (or False) means it doesn't.

# For weighted graphs: the actual weight is stored.

# A -- B
# |    |
# C -- D

# index mapping:
# 0 → A
# 1 → B
# 2 → C
# 3 → D


# Adjacency Matrix Representation of the above graph:
#   A  B  C  D
# A 0  1  1  0
# B 1  0  0  1
# C 1  0  0  1
# D 0  1  1  0
# Pros:
# - Simple and easy to implement.
# - Fast to check if an edge exists between two vertices (O(1)).
# - Good for dense graphs where the number of edges is close to the maximum possible.
# Cons:
# - Uses O(V^2) space, which can be inefficient for sparse graphs.
# - Iterating through all edges takes O(V^2) time.
# - Adding a vertex requires resizing the matrix, which can be costly.
# - Removing a vertex requires O(V^2) time to update the matrix.
# - Not suitable for graphs with a large number of vertices and few edges.
# - Not suitable for dynamic graphs where edges are frequently added or removed.


class GraphMatrix:
    def __init__(self, vertices):
        """Initialize the graph with a list of vertices."""
        """Create a mapping of vertices to indices and initialize the adjacency matrix."""
        """The adjacency matrix is initialized with zeros, indicating no edges between vertices."""
        """The size of the matrix is determined by the number of vertices."""
        """The vertex_index dictionary maps each vertex to its corresponding index in the matrix."""
        """The matrix is a 2D list initialized with zeros, representing no edges between any vertices."""
        self.vertices = vertices
        self.size = len(vertices)
        self.vertex_index = {v: i for i, v in enumerate(vertices)}
        self.matrix = [[0] * self.size for _ in range(self.size)]

    def add_edge(self, v1, v2):
        """Add an edge between two vertices v1 and v2."""
        """This method updates the adjacency matrix to indicate the presence of an edge between the specified vertices."""
        """The vertices are first mapped to their corresponding indices using the vertex_index dictionary."""
        """The matrix is then updated to reflect the edge by setting the corresponding entry to 1."""
        """Since this is an undirected graph, the matrix is updated symmetrically for both vertices."""
        """The method does not return any value, but modifies the internal state of the graph."""
        i = self.vertex_index[v1]
        j = self.vertex_index[v2]
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1  # For undirected graph

    def display(self):
        """Display the adjacency matrix in a readable format."""
        """This method prints the adjacency matrix to the console, along with the corresponding vertex labels."""
        """The first row and column are labeled with the vertex names for clarity."""
        """The matrix is printed in a grid format, where each row corresponds to a vertex and its connections."""
        """The method does not return any value, but provides a visual representation of the graph."""
        print("  ", " ".join(self.vertices))
        for i in range(self.size):
            row = [str(self.matrix[i][j]) for j in range(self.size)]
            print(self.vertices[i], " ".join(row))




g = GraphMatrix(['A', 'B', 'C', 'D'])

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

g.display()

class Graphwithoutmapping:
    def __init__(self, vertices):
        """Initialize the graph with a given number of vertices."""
        """Create an adjacency matrix of size vertices x vertices, initialized with zeros."""
        """The adjacency matrix is a 2D list where each entry represents the presence of an edge between two vertices."""
        """The size of the matrix is determined by the number of vertices."""
        """The matrix is initialized with zeros, indicating no edges between any vertices."""
        """The method does not return any value, but sets up the internal state of the graph."""
        self.V = vertices  # Number of vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]  # Initialize adjacency matrix with 0s

    def add_edge(self, u, v, weight=1):
        """Add an edge from vertex u to vertex v with the given weight."""
        """This method updates the adjacency matrix to indicate the presence of an edge between the specified vertices."""
        """The vertices are represented by their indices in the matrix."""
        """The matrix is updated to reflect the edge by setting the corresponding entry to the specified weight."""
        """Since this is an undirected graph, the matrix is updated symmetrically for both vertices."""
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight  # For undirected graph

    def remove_edge(self, u, v):
        """Remove the edge from vertex u to vertex v."""
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0  # For undirected graph

    def display(self):
        """Display the adjacency matrix."""
        for row in self.adj_matrix:
            print(row)



class GraphDirected:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]  # Initialize adjacency matrix with 0s

    def add_edge(self, u, v, weight=1):
        """Add an edge from vertex u to vertex v with the given weight."""
        self.adj_matrix[u][v] = weight

    def remove_edge(self, u, v):
        """Remove the edge from vertex u to vertex v."""
        self.adj_matrix[u][v] = 0

    def display(self):
        """Display the adjacency matrix."""
        for row in self.adj_matrix:
            print(row)


