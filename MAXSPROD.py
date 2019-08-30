class Solution:
    # @param A : list of integers
    # @return an integer
    
    def max_index(self, A):
        stack_lj = []
        max_lj = []
        for i in range(len(A)):
            lj = -1
            while stack_lj and stack_lj[-1][1]<=A[i]:
                stack_lj.pop()
            if stack_lj:
                lj = stack_lj[-1][0]
            stack_lj.append([i,A[i]])
            max_lj.append(lj)
        return max_lj
        
    def maxSpecialProduct(self, A):
        
        ans = 0
        
        max_lj = self.max_index(A)
        max_rj = self.max_index(A[::-1])[::-1]
        new_max_rj = []

        for elem in max_rj:
            if elem!=-1:
                new_max_rj.append(len(A)-elem-1)
            else:
                new_max_rj.append(0)
        # print max_lj
        # print new_max_rj

        for i in range(len(A)):
            ans = max(ans, (max_lj[i]*(new_max_rj[i])))
            
        return ans%1000000007

s = Solution()
print s.maxSpecialProduct([ 5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9 ])