# Транспонирование матриц
А = [[1,2,3],
[45,67,23]]
B = [[6,7],
[45,78],
[90,78]]
matrix = [[0,0],
          [0,0]]
# умножение матриц
for i in range(len(A)):
   for j in range(len(B[0])):
        for k in range(len(B)):
           resultant_matrix[i][j] += A[i][k] * B[k][j]
for r in matrix:
   print(r)
# определение ранга
class rankMatrix(object):
	def __init__(self, Matrix):
		self.R = len(Matrix)
		self.C = len(Matrix[0])
	def swap(self, Matrix, row1, row2, col):
		for i in range(col):
			temp = Matrix[row1][i]
			Matrix[row1][i] = Matrix[row2][i]
			Matrix[row2][i] = temp
	def Display(self, Matrix, row, col):
		for i in range(row):
			for j in range(col):
				print (" " + str(Matrix[i][j]))
			print ('\n')

	def rankOfMatrix(self, Matrix):
		rank = self.C
		for row in range(0, rank, 1):
			if Matrix[row][row] != 0:
				for col in range(0, self.R, 1):
					if col != row:
						multiplier = (Matrix[col][row] /
									Matrix[row][row])
						for i in range(rank):
							Matrix[col][i] -= (multiplier *
											Matrix[row][i])
	
			else:
				reduce = True
				
				
				for i in range(row + 1, self.R, 1):
					if Matrix[i][row] != 0:
						self.swap(Matrix, row, i, rank)
						reduce = False
						break
						
				
				if reduce:
					rank -= 1
					for i in range(0, self.R, 1):
						Matrix[i][row] = Matrix[i][rank]
						
				
				row -= 1
				
		
		return (rank)


if __name__ == '__main__':
	Matrix = [[10, 20, 10],
			[-20, -30, 10],
			[30, 50, 0]]
	RankMatrix = rankMatrix(Matrix)
	print ("Ранг матрицы:",
		(RankMatrix.rankOfMatrix(Matrix)))
