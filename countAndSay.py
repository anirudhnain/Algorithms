class Solution:
	def countAndSay(self, n):
		res = "1"
		for k in range(n-1):
			currentString = res
			res = ""
			freq = 1
			for i,elem in enumerate(currentString):
				if i == 0:
					continue
				if elem == currentString[i-1]:
					freq += 1
				else:
					res += str(freq)+currentString[i-1]
					freq = 1
			res += str(freq)+currentString[i]
		return res
s = Solution()
print(s.countAndSay(4))