class Solution:
    # @param a : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, a, n, d):
        res = 1
        while(n>0):
            if (n%2==1):
                res = (res*a)%d
            a = (a*a)%d
            n >>=1
        return res%d

s = Solution()
print (s.pow(0, 0, 5))