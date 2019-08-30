class Solution():
	def reverseBits(self, number):
		res = 0
		i = 31
		while number:
			if number%2==1:
				res += 1<<i
			number=number>>1
			i-=1
		return res
print (Solution().reverseBits(3))