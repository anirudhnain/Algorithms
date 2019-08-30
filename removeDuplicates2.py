class Solution:
	def removeDuplicatesForSorted2(self, A):
		i = j = 0

		lastSwapped = None
		while i<len(A) and j<len(A):
			
			if j<i:
				j=i+1
			
			if j<len(A):
				startj = j
				lastSwapped = A[j]
			
			while i<len(A) and j<len(A) and A[j]==lastSwapped and j-startj<2:
				A[i],A[j] = A[j],A[i]
				i+=1
				j+=1

			while j<len(A) and A[j]==lastSwapped:
				j+=1

		return A

s = Solution()
print(s.removeDuplicatesForSorted2([1,1,1,2,3,3,3]))