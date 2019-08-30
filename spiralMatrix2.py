class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        arr = [[0 for i in range(n)] for j in range(n)]
        
        iterator = int(n/2) if n%2==0 else int(n/2)+1
        lastNumber = 1
        
        for k in range(iterator):    
            produceNumber = n-2*k
            for i in range(lastNumber, lastNumber+produceNumber):
                arr[k][i-lastNumber+k] = i
            # print (arr,i)
            lastNumber = i    
            for i in range(lastNumber,lastNumber+produceNumber):
                arr[(k)+(i-lastNumber)][n-1-k] = i
            # print (arr,i)
            lastNumber = i   
            for i in range(lastNumber,lastNumber+produceNumber):
                arr[n-1-k][(n-1-k)-(i-lastNumber)] = i
            # print (arr,i)
            lastNumber = i
            for i in range(lastNumber,lastNumber+produceNumber-1):
                arr[(n-1-k)-(i-lastNumber)][k] = i
            # print (arr,i)
            lastNumber = i+1
        return arr

s = Solution()
print (s.generateMatrix(4))