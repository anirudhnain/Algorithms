class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 0 
        if not A:
            return 0
        lastReversed = None
        j = 0
        while j<len(A):
            if j==0:
                j+=1
                continue
            if A[j]!=A[j-1] and A[j]!=lastReversed:
                lastReversed = A[j-1]
                A[i],A[j-1] = A[j-1],A[i]
                i+=1
            j+=1
        if A[j-1]!=lastReversed:
            A[i],A[j-1] = A[j-1],A[i]
        return i+1

s = Solution()
print (s.removeDuplicates([ 0, 0, 1, 1, 2, 2, 3 ]))