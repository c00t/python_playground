import numpy as np

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_np = np.array(matrix)
print(matrix_np)
print(matrix_np * 2)

A = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(A @ A)

print(list(range(0, 10)))
print(np.arange(0, 10))

print(np.arange(0, 10, 2))