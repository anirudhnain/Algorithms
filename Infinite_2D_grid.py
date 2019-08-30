class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        ans = 0
        n = len(A)
        
        if n<2:
            return 0
            
        for i in range(n-1):
            diff_x = abs(A[i+1]-A[i])
            diff_y = abs(B[i+1]-B[i])
            
            ans += max(diff_x, diff_y)
            
        return ans

s = Solution()
print s.coverPoints([ 4, 8, -7, -5, -13, 9, -7, 8 ], [ 4, -15, -10, -3, -13, 12, 8, -8 ])