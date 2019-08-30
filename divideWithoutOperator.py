class Solution(object):
    def divide(self, dividend, divisor):
        negative = 1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            negative = -1
                        
        divisor,dividend = abs(divisor), abs(dividend)

        increment = divisor
        ans = 0
        jumps = 0
        
        if dividend == divisor:
            return 1*negative

        while increment<=dividend:
            increment = increment<<1
            jumps+=1
            if increment>dividend:
                ans += 1 << (jumps-1)
                jumps = 0
                dividend -= increment >> 1
                increment = divisor
        
        return min(max(-2147483648, ans*negative), 2147483647)

s = Solution()
print (s.divide(-2147483648,2))