	class Solution:
	    # @param A : string
	    # @return a list of integers
	    def flip(self, string):
	        allOnes = True
	        
	        for elem in string:
	            if elem != '1':
	                allOnes = False
	                break
	        
	        if allOnes:
	            return []
	            
	        arr = [0]*len(string)
	            
	        for i in range(len(string)):
	            if string[i] == '0':
	                arr[i] = 1
	            else:
	                arr[i] = -1
	        
	        tempSum = 0
	        maxSum = 0
	        startIndex = 0
	        ans = [0,0]

	        print arr
	        
	        for i in range(len(string)):
	            tempSum += arr[i]
	            # print tempSum
	            if tempSum<0:
	                tempSum = 0
	                startIndex = i+1
	            if tempSum>maxSum:
	                ans[0] = startIndex+1
	                ans[1] = i+1
	                maxSum = tempSum
	        
	        return ans

f = Solution()
print f.flip("0100")


[6,5,4,3,2,1]		[1,3,2,5,6,4] [3,1,5,2,6,4]

[6,4,5,2,3,1]

[1,2,3,4,5,6]
[2,1,4,3,6,5]