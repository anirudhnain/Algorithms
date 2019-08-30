class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        
        lo = 0
        hi = len(A)
        
        while lo<hi:
            mi = (lo+hi)>>1
            if A[mi] == B:
                return mi
            elif A[mi]<B:
                lo = mi+1
            else:
                hi = mi
        return lo

s = Solution()
print(s.searchInsert([1, 3, 5, 6 ], 4))