class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        
        
        n = len(A)
        
        
        add = [0]*n
        subtract = [0]*n
        
        for i in range(0, n):
            add[i] = A[i]+i
            subtract[i] = A[i]-i
            
        ans = max(abs(max(add)-min(add)), abs(max(subtract)-min(subtract)))
            
        return ans
            
s = Solution()
print s.maxArr([ 61, 35, 50, 2, 29, 29, 97, 47, 28, 36, 45, 67, 60, 70, 56, 32, 63, 36, 72, 52, 41, 32, 48, 28, 60, 32, 34, 67, 86, 15, 47, 30, 61, 34, 51, 49, 27, 30, 81, 45, 43, 63, 66, 70, 38, 32, 68, 42, 72, 41 ])