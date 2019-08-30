class Solution:
    def getRequiredPainters(self, arr,n, maxLengthPerPainter):
      total = 0
      numPainters = 1
      for i in range(n):
        total += arr[i]
        if (total > maxLengthPerPainter):
          total = arr[i]
          numPainters+=1
      return numPainters
    
    def partition(self,arr,k):
      lo = max(arr)
      hi = sum(arr)
     
      while (lo < hi) :
        mid = lo + int((hi-lo)>>1)
        requiredPainters = self.getRequiredPainters(arr, len(arr), mid)
        if (requiredPainters <= k):
          hi = mid
        else:
          lo = mid+1
      return lo

    def paint(self,k,T,arr):
        return (self.partition(arr,k)*T)% 10000003

s = Solution()
print(s.paint(1,1000000,[1000000,1000000]))