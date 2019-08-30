class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

    	last_index_numbers = {}

        A.sort()

    	for i in range(len(A)):
    		last_index_numbers[A[i]] = i

        for i in range(len(A)):
            if (len(A)-i-1)-(last_index_numbers[A[i]]-i) == A[i]:
                return 1
        return -1

s = Solution()
print s.solve([1,1,1,2,4,3])