class Solution():

	def minXOR(self, arr):

		minVal = 0
		arr.sort()
		ans = max(arr)
		for i in range(1, len(arr)):
			ans = min(arr[i]^arr[i-1],ans)
		return ans