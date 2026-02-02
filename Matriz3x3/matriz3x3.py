import numpy as np

matriz_A = np.array([[1,2,3], [4,5,6], [7,8,9]])
print('This is the matrix A 3x3')
print(matriz_A)
matriz_B = np.array([[3,5,7], [1,8,1], [4,2,1]])
print('This is the matrix B 3x3')
print(matriz_B)
matriz_C = matriz_A * matriz_B
print('The result of multiplication A*B = C')
print(matriz_C)
