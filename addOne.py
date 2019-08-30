class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        
        carry = 0
        add = 1
        
        while A and A[0] == 0 and len(A)>1:
            A.pop(0)
        
        for i in range(len(A)-1, -1, -1):
            elem = A[i]
            if elem == 9:
                carry = 1
                add = 0
                A[i] = 0
            else:
                A[i]+= carry+add
                carry = 0
                break
        
        if carry == 1:
            A.insert(0,1)
        
        return A

s = Solution()
print s.plusOne([0,0,0])