import numpy as np
class graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.adj_matrix = self.get_adj_matrix()

    def get_adj_matrix(self):
        matrix = np.zeros([len(self.nodes), len(self.nodes)], dtype=int)
        for edge in self.edges:
                matrix[edge[0]-1][edge[1]-1] = self.edges[edge]
                matrix[edge[1]-1][edge[0]-1] = self.edges[edge]
        
        return matrix
    
    def prim(self, starting_node):

        result = {}
        N = len(self.nodes)
        adj_matrix = self.adj_matrix
        is_selected = [0]*N
        num_of_edges = 0

        is_selected[self.nodes.index(starting_node)] = True

        while (num_of_edges < N - 1):
            minimum = adj_matrix.max()
            a, b = 0, 0

            for y in range(N):

                if is_selected[y]:
                    for x in range(N):

                        if not is_selected[x] and adj_matrix[y][x]:  
                            if minimum > adj_matrix[y][x]:
                                minimum = adj_matrix[y][x]
                                a, b = y, x

            result[(a+1, b+1)] = adj_matrix[a][b]
            is_selected[b] = True
            num_of_edges += 1
        
        print(result)
                
                 
        



nodes = [1, 2, 3, 4, 5, 6, 7]


edges = {(1, 2): 1, (1, 4): 3, (1, 6): 1, (1, 7): 3, (2, 7): 2, (2, 6): 1, (2, 5): 1, (2, 3): 3, (3, 5): 2, (3, 4): 1, (4, 5): 2, (4, 6): 2, (6, 7): 2}

G = graph(nodes, edges)
G.prim(1)


