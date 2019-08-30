class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        reverse_A = len(A)-1
        longestMatching = 0
        temp = 0
        A_pointer = 0
        i = 0

        print (reverse_A,len(A))
        while reverse_A >i:
            if A[A_pointer] == A[A_pointer]:
                temp+=1
                A_pointer+=1
                i+=1
            else:
                if A_pointer == 0:
                    i+=1
                else:
                    A_pointer = 0
                temp = 0
            longestMatching = max(longestMatching, temp)
                
        return len(A)-longestMatching

# heymfleylfmyeh
# ye
eeylfpbnpljvrvipyamyeehwqnq

s = Solution()
print(s.solve("eylfpbnpljvrvipyamyehwqnq"))