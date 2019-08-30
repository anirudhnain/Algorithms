class Solution:
    # @param A : tuple of integers
    # @return a strings
    def letter_cmp(self, a, b):
        if int(a+b) > int(b+a):
            return -1
        elif int(a+b) < int(b+a):
            return 1
        return 0
    
    def largestNumber(self, A):
        allZero = True
        for elem in A:
            if elem != 0:
                allZero = False
                break
            
        if allZero:
            return '0'
        
        A = [str(e) for e in A]
        A.sort(self.letter_cmp)
        return ''.join(A)
s = Solution()
print (s.largestNumber([3, 30, 34, 5, 9]))
