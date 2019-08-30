class Solution():
	def pascalTraingle(self, number):
		ans = []
		if number<1:
			return []
		if number == 1:
			return [[1]]
		if number == 2:
			return [[1],[1,1]]

		ans = [[1],[1,1]]
		for i in range(2, number):
			lastRow = ans[-1]
			newRow = []
			for i in range(len(lastRow)):
				if i == 0:
					newRow.append(lastRow[i])
				else:
					newRow.append(lastRow[i]+lastRow[i-1])
			newRow.append(lastRow[-1])
			ans.append(newRow)
		return ans

s = Solution()
print (s.pascalTraingle(5))
