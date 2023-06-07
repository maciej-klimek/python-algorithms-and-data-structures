import numpy as np

class graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.adj_matrix = self.get_adj_matrix(nodes, edges)

    def get_adj_matrix(self, nodes, edges):
        matrix = np.zeros([len(nodes), len(nodes)])
        for edge in edges:
                matrix[edge[0]-1][edge[1]-1] = edges[edge]
                matrix[edge[1]-1][edge[0]-1] = edges[edge]
        
        return matrix




nodes = [1, 2, 3, 4, 5, 6, 7]

edges = {(1, 2): 2, (1, 5): 4, (1, 7): 3, (2, 3): 4, (2, 5): 2, (3, 5): 2, (3, 6): 2, (3, 4): 2, (4, 6) : 2, (6, 5): 1, (6, 7): 3, (7, 5): 3}

G = graph(nodes, edges)

