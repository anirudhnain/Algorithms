class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        
        sorted_A = sorted(A)
        start = len(A)
        end = 0
        already_sorted = True

        print A,sorted_A

        for i in range(len(A)):
            if sorted_A[i] != A[i]:
                print i
                start = min(start,i)
                end = max(end,i)
                already_sorted = False
        if already_sorted:
            return [-1]
        return [start,end]

s = Solution()
print s.subUnsort([1,3,2,4,5])