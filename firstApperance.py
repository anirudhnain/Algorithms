class Solution():
	def firstAppearnce(self, A, target):
		lo = 0
		hi = len(A)

		while(lo<hi):
			mi = (lo+hi)>>1
			if A[mi]<target:
				lo=mi+1
			else:
				hi = mi
		return hi


s = Solution()
print(s.firstAppearnce([1,1,1,4,5,6,9,9], 9))