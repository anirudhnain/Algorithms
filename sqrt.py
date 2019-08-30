class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        lo = 0
        hi = A

        if A==1 or A==0:
            return A
        
        mi = (lo+hi)>>1
        
        while lo<hi:
            mi = (lo+hi)>>1
            p = mi*mi
            if p == A:
                return mi
            elif p<A:
                lo = mi+1
            else:
                hi = mi
        return lo-1
s  = Solution()
print(s.sqrt(20))