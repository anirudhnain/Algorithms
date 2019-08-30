class Solution():
	def antiDiagnols(self, matrix):

		n = len(matrix)
		ans = []
		#generate for row 0
		for i in range(n):
			r = 0
			c = i
			row = []
			while 0<=r<n and 0<=c<n:
				row.append(matrix[r][c])
				r+=1
				c-=1
			# print (row)
			ans.append(row)

		#generate for column n-1
		for i in range(1,n):
			c= n-1
			r = i
			row = []
			while 0<=r<n and 0<=c<n:
				row.append(matrix[r][c])
				r+=1
				c-=1
			# print (row)
			ans.append(row)
		return ans

s = Solution()
print (s.antiDiagnols([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))