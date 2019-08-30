class Solution():
	def checkIfMidIsValid(self, num, arr, m):
		localSum = 0
		breaks = 0
		for i in range(len(arr)):
			if breaks>=m:
				return False
			localSum+=arr[i]
			if localSum>num:
				breaks += 1
				localSum = arr[i]
				if localSum>num:
					return False
		# print("Outside:",localSum, num,breaks)
		if localSum>num or breaks>=m:
			return False
		return True


	def allocateBooks(self, arr, m):

		if m>len(arr):
			return -1

		lo = min(arr)
		hi = sum(arr)

		while lo<hi:
			mi = (lo+hi)>>1
			# print (mi, self.checkIfMidIsValid(mi, arr, m))
			if (self.checkIfMidIsValid(mi, arr, m)):
				hi = mi
			else:
				lo = mi+1
		return lo
s = Solution()
print(s.allocateBooks([34, 90, 67, 12], 4))