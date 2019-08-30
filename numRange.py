class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        
        lo = min(B,C)
        hi = max(B,C)
        
        a = b = -1
        ans = 0
        sum_a = sum_b = A[0]
        moved = False
        n = len(A)
        for i in range(n):
            sum_a -= A[i]
            sum_b -=A[i]
            while a<n and  sum_a< lo:
                a += 1
                if a<n:
                    sum_a += A[a]
            while b<n and sum_b <= hi:
                b += 1
                if b<n:
                    sum_b += A[b]
            for j in range(a, b):
                print(A[i:j+1])
            
        return ans
s = Solution()
print(s.numRange([ 80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90 ], 99, 269))