class Solution():
	def checkTripletsExists(self, arr):
		sum2Numbers = {}

		for i in range(len(arr)):
			for j in range(i,len(arr)):
				sum2Numbers[arr[i]+arr[j]] = set()
				sum2Numbers[arr[i]+arr[j]].add(arr[i])
				sum2Numbers[arr[i]+arr[j]].add(arr[j])

		for i in range(len(arr)):
			

