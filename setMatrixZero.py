	class Solution:

		def setRowZero(self, matrix, row):
			for i in range(len(matrix[0])):
				if matrix[row][i]!=2:
					matrix[row][i] = 0

		def setColZero(self, matrix, col):
			for i in range(len(matrix)):
				if matrix[i][col]!=2:
					matrix[i][col] = 0

		def setZeroes(self, matrix):
			n = len(matrix)

			if not matrix:
				return []
		
			for i in range(n):
				for j in range(n):
					if matrix[i][j] == 0:
						matrix[i][j] = 2
		
			for i in range(n):
				for j in range(len(matrix[0])):
					if matrix[i][j] == 2:
						self.setRowZero(matrix, i)
						break

			for j in range(len(matrix[0])):
				for i in range(n):
					if matrix[i][j] == 2:
						self.setColZero(matrix, j)
						break

			for i in range(n):
				for j in range(n):
					if matrix[i][j] == 2:
						matrix[i][j] = 0

			return matrix

s = Solution()
a = s.setZeroes([[1,0,1],[1,1,1],[0,1,1]])
for row in a:
	print (row)