import sys
class Solution():
    def __init__(self):
        self.cache = []

    def recursePoint(self, arr, endIndex, k, precomputeSum):
        if self.cache[endIndex][k]:
            return self.cache[endIndex][k]
        if k==1:
            self.cache[endIndex][k] = sum(arr[:endIndex])
            return self.cache[endIndex][k]
        if endIndex==1:
            self.cache[endIndex][k] = arr[0]
            return self.cache[endIndex][k]

        ans = sys.maxsize
        for partitionPoint in range(1, endIndex):
            ans = min(max(precomputeSum[partitionPoint][endIndex-1], 
                self.recursePoint(arr, partitionPoint, k-1, precomputeSum)), ans)
        self.cache[endIndex][k] = ans
        return ans

    def paint(self,k, T,arr):
        precomputeSum = [[0 for i in range(len(arr))] for j in range(len(arr))]
        for i in range(len(arr)):
            precomputeSum[0][i] = arr[i]+precomputeSum[0][i-1]
        for i in range(1,len(arr)):
            for j in range(i,len(arr)):
                precomputeSum[i][j] = precomputeSum[i-1][j]-arr[i-1]
        self.cache = [[None for i in range(k+1)] for j in range(len(arr)+1)]
        return (self.recursePoint(arr,len(arr),k, precomputeSum)*T)% 10000003

s = Solution()
print(s.paint(1,1000000,[1000000,1000000]))