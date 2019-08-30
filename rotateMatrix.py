class Solution():

	def printMatrix(self, matrix):
		for elem in matrix:
			print elem

	def rotateMatrix(self, matrix):

		if not matrix:
			return []

		len_matrix = len(matrix)

		for j in range(len(matrix)/2):
			for i in range(j,len(matrix)-1-j):

				# print j,i

				#4 way roataion
				replacedValue = matrix[i][len_matrix-j-1]
				matrix[i][len_matrix-j-1] = matrix[j][i]

				# print i,len_matrix-j-1
				# print "First Rotation"
				# print self.printMatrix(matrix)

				previousValue = matrix[len_matrix-j-1][len_matrix-i-1]
				matrix[len_matrix-j-1][len_matrix-i-1] = replacedValue
				replacedValue = previousValue
				# print "Second Rotation"
				# print self.printMatrix(matrix)
				# print len_matrix-j-1,len_matrix-i-1

				previousValue = matrix[len_matrix-i-1][j]
				matrix[len_matrix-i-1][j] = replacedValue  
				replacedValue = previousValue

				# print len_matrix-i-1,j

				# print "Third Rotation"
				# print self.printMatrix(matrix)

				matrix[j][i] = replacedValue

s  = Solution()
original_matrix = [[0,1,2,4],[3,8,7,9],[14,15,16,17],[20,21,22,23]]
s.rotateMatrix(original_matrix)