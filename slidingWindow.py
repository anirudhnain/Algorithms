class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        stack = []
        ans = []
        if B>len(A):
            return 
        for i in range(B-1):
            elem = A[i]
            while stack and elem>stack[-1][0]:
                stack.pop()
            stack.append([elem,i])
        l = 0
        for i in range(B-1, len(A)):
            elem = A[i]
            while stack and elem>stack[-1][0]:
                stack.pop()
            stack.append([elem,i])
            print stack
            ans.append(stack[0][0])
            if stack and stack[0][1]<l:
                stack.pop(0)
            l += 1
        return ans
s = Solution()
print s.slidingMaximum([1,3,-1,-3,5,3,6,7],3)