class Solution:
	def maximumGap(self, A):

		maxRightNumbers = []
		minLeftNumbers = []

		for elem in A:
			if not minLeftNumbers or elem<minLeftNumbers[-1]:
				minLeftNumbers.append(elem)
			else:
				minLeftNumbers.append(minLeftNumbers[-1])

		for elem in reversed(A):
			if not maxRightNumbers or elem>maxRightNumbers[-1]:
				maxRightNumbers.append(elem)
			else:
				maxRightNumbers.append(maxRightNumbers[-1])
		maxRightNumbers = maxRightNumbers[::-1]

		# print (minLeftNumbers, maxRightNumbers)

		i=j=0
		ans = 0
		while i<len(minLeftNumbers) and j<len(maxRightNumbers):
			if minLeftNumbers[i]>maxRightNumbers[j]:
				i+=1
			else:
				j+=1
			# print (i,j)
			if i<len(A) and j<len(A) and A[j]>=A[i]:
				ans = max(ans, j-i)

		return ans

s =  Solution()
print (s.maximumGap([5,3,2,4]))