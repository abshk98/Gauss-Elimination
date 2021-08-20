import numpy as np
A = np.array([[-6.0, 4.0, 0.0, 0.0],
               [0.0, -7.0, 3.0, 4.0],
               [4.0, 0.0, -4.0, 0.0],
               [2.0, 0.0, 1.0, -4.0]])
B = np.array([-50.0, 0.0, 0.0, -50.0])
print(np.linalg.solve(A, B))
