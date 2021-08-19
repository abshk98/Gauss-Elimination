import numpy as np
A = np.array([[-6.0, 4.0, 0.0, 0.0],
              [0.0, -7.0, 3.0, 4.0],
              [4.0, 0.0, -4.0, 0.0],
              [2.0, 0.0, 1.0, -4.0]])
B = np.array([-2.25, 0, 0, -1.5])
n = len(B)

for k in range(0, n-1):
    for i in range(k+1, n):
        ratio = A[i, k]/A[k, k]
        for j in range(k, n):
            A[i, j] = A[i, j] - ratio*A[k, j]
        B[i] = B[i] - B[k]*ratio

x = np.zeros(n)
x[n-1] = B[n-1]/A[n-1, n-1]
for i in range(n-2, -1, -1):
    sum_j = 0
    for j in range(i+1, n):
        sum_j += A[i, j]*x[j]
    x[i] = (B[i] - sum_j)/A[i, i]

print(x)



