import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 1, 0, 2, 0, 4, 1, 0, 2])

print(csr_matrix(arr))
