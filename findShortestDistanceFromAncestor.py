class Solution():
	def solution(self, dis, A):

		res = []

		for child,parent in enumerate(A):
			parent = child
			D = dis
			while D>-1 and parent!=-1:
				parent = A[parent]
				D-=1
			res.append(parent)
		return res

s = Solution()
print(s.solution(2, [-1,0,4,2,1]))