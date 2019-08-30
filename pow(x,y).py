class Solution(object):
    
    def getPow(self, currentVal, mutiplicationPow, mutiplicationVal, x, currentPow, abs_n):
        
        if currentPow == abs_n:
            return currentVal

        currentVal *= mutiplicationVal
        currentPow += mutiplicationPow

        if (mutiplicationPow<<1) <= (abs_n-currentPow) :
        	mutiplicationPow = mutiplicationPow<<1
        	mutiplicationVal *= mutiplicationVal
        else:
            mutiplicationPow = 1
            mutiplicationVal = x

        return self.getPow(currentVal, mutiplicationPow, mutiplicationVal, x, currentPow, abs_n)
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n==0:
            return 1
       
        result = self.getPow(x,1,x,x,1,abs(n))

        if n<0:
        	return 1.0/result
        else:
        	return result

s = Solution()
val = 5
power = -4
print s.myPow(val, power)
print val**power