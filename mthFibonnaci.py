class Solution:
    def mthFibonnaci(self, n):
        q = [[1, 1], [1, 0]]
        res = self.pow(q, n)
        return res[0][0]

    def pow(self, a, n):
        res = [[1,0],[0,1]]
        while(n>0):
            if (n%2==1):
                res = self.multiply(res,a)
            a = self.multiply(a,a)
            n >>=1
        return res
    
    def multiply(self, a,b):
        c = [[None for i in range(2)] for i in range(2)];
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c

s= Solution()
print(s.mthFibonnaci(6))

# [Fn Fn-2
#  Fn-1 Fn-3]

# [1,1
# 1,0]


# Fn+1      Fn-1
# Fn        Fn-2          