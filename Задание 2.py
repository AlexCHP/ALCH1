#транспонирование
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = matrix.T
print(result)
#умножение матриц
import numpy as np
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
c = np.mul(a, b)
print(c)
#ранг
import numpy as np
matrixA = np.array([[1, 2, 3, 23],
                       [4, 5, 6, 25],
                       [7, 8, 9, 28],
                       [10, 11, 12, 41]])
print("Ранг матрицы: ", np.linalg.matrix_rank(matrixA))
