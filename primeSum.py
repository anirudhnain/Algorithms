class Solution:
    # @param A : integer
    # @return a list of integers
    def isPrime(self, integer):
        i = 2
        while i*i<=integer:
            if integer%i==0:
                return False
            i+=1
        return True
    
    def primesum(self, A):
                    
        i = 2
        j = A
        
        while i<=j:
            sum_i_j = i+j
            if sum_i_j == A and self.isPrime(i) and self.isPrime(j):
                return [i,j]
            elif sum_i_j>A:
                j-=1
            else:
                i+=1

s = Solution()
print s.primesum(8)