class Solution:
	def pairWiseHamming(self, A):
		bits = [0]*32

		for elem in A:
			temp = elem
			i = 0
			while temp!=0:
				bits[i] += temp%2
				temp = temp >> 1
				i+=1
		ans = 0
		for i in range(32):
			ans+= bits[i]*(len(A)-bits[i])
		return ans

s  = Solution()
print(s.pairWiseHamming([4,14,2]))

# 0010
# 0100
# 1110