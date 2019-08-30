class Solution:
    def removeElements(self, A, B):
        i = 0
        for j in range(len(A)):
            if A[j] != B:
                A[i],A[j] = A[j],A[i]
                i+=1
        return i+1

s = Solution()
print(s.removeElements([ 1, 3, 3, 3, 2 ], 3))