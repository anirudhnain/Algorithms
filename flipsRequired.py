class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, arr, m):
        n = len(arr)
      
        wL = wR = 0
      
        bestL = bestWindow = 0
      
        zeroCount = 0
      
        while wR < n: 
              
            if zeroCount <= m : 
                if arr[wR] == 0 : 
                    zeroCount += 1
                wR += 1
      
            if zeroCount > m : 
                if arr[wL] == 0 : 
                    zeroCount -= 1
                wL += 1
      
            if wR - wL > bestWindow : 
                bestWindow = wR - wL 
                bestL = wL 
            
        return [x for x in range(bestL, bestL+bestWindow)]

s = Solution()
s.maxone()