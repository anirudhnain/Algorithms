class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = []
        maxArea = 0
        forwardScan = [0]*len(A)
        backScan = [0]*len(A)
        for index,elem in enumerate(A):
            if not stack:
                stack.append([index,elem])
            else:
                if elem>stack[-1][1]:
                    prevIndex = index
                else:
                    while stack and elem<=stack[-1][1]:
                        prevIndex, num1 = stack.pop()
                        forwardScan[prevIndex] = num1*(index-prevIndex)
                stack.append([index,elem])
            # print stack, forwardScan
        while stack:
            prevIndex, num1 = stack.pop()
            forwardScan[prevIndex] = num1*(len(A)-prevIndex)
            # print stack, forwardScan

        stack = []
        for index,elem in enumerate(A[::-1]):
            if not stack:
                stack.append([index,elem])
            else:
                if elem>stack[-1][1]:
                    prevIndex = index
                else:
                    while stack and elem<stack[-1][1]:
                        prevIndex, num1 = stack.pop()
                        backScan[prevIndex] = num1*(index-prevIndex-1)
                stack.append([index,elem])
        while stack:
            prevIndex, num1 = stack.pop()
            backScan[prevIndex] = num1*(len(A)-prevIndex-1)
        backScan = backScan[::-1]

        # print forwardScan
        # print backScan
        for i in range(len(A)):
            maxArea = max(maxArea, forwardScan[i]+backScan[i])
        return maxArea

s = Solution()
print s.largestRectangleArea([1,1])
# print s.largestRectangleArea([ 2, 74, 5, 25, 60, 10, 93, 58, 95, 20, 28, 80, 76, 28, 75, 100, 2, 73, 42, 34, 66, 51, 89, 85, 73, 10, 43 ])
# print s.largestRectangleArea([ 47, 69, 67, 97, 86, 34, 98, 16, 65, 95, 66, 69, 18, 1, 99, 56, 35, 9, 48, 72, 49, 47, 1, 72, 87, 52, 13, 23, 95, 55, 21, 92, 36, 88, 48, 39, 84, 16, 15, 65, 7, 58, 2, 21, 54, 2, 71, 92, 96, 100, 28, 31, 24, 10, 94, 5, 81, 80, 43, 35, 67, 33, 39, 81, 69, 12, 66, 87, 86, 11, 49, 94, 38, 44, 72, 44, 18, 97, 23, 11, 30, 72, 51, 61, 56, 41, 30, 71, 12, 44, 81, 43, 43, 27 ])