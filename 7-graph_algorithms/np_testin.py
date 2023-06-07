import numpy as np


matrix = np.zeros([3, 3])
edges = {(1, 2): 1, (2, 3): 2, (1, 4): 5}

#for edge in edges:
#    print(edges[edge])

matrix[0][0] = 1
print(matrix)