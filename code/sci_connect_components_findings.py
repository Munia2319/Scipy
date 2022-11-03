import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0],
  [0, 0, 0],
  [0, 0, 2]
])

newarr = csr_matrix(arr)

print(connected_components(newarr))
