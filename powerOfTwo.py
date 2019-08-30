class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        
        sqrt_A = A**(0.5)
        
        for i in xrange(2, int(sqrt_A)+1):
            temp_A = A*1.0
            while(temp_A == int(temp_A) and temp_A!=1.0):
                # print temp_A
                temp_A /= i
                continue
            
            if temp_A == 1.0:
                return 1
                
        return 0

s = Solution()
print s.isPower(2100000000000)