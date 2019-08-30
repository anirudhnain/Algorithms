class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        totalWater = 0
        maxStack = []
        maxStackR = []
        for elem in A:
            if not maxStack:
                maxStack.append(elem)
            else:
                maxStack.append(max(maxStack[-1],elem))
        for elem in A[::-1]:
            if not maxStackR:
                maxStackR.insert(0, elem)
            else:
                maxStackR.insert(0, max(maxStackR[0],elem))
                
        for i in range(len(A)):
            totalWater +=  abs(min(maxStackR[i],maxStack[i])-A[i])
        return totalWater
s =  Solution()
print s.trap([ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ])