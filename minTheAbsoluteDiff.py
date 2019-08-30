import sys
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        
        #Big idea: always increment the min one
        
        i=j=k=0
        minDiff = sys.maxsize
        while i<len(A) and j<len(B) and k<len(C):
            print(i,j,k)
            minElem = min(A[i],B[j],C[k])
            minDiff = min(minDiff, max(A[i], B[j], C[k])-minElem)
            if minElem == A[i]:
                i+=1
            if minElem == B[j]:
                j+=1
            if minElem == C[k]:
                k+=1
                
        return minDiff
s = Solution()
print (s.solve([ 1, 4, 5, 8, 10 ], [ 6, 9, 15 ],  [ 2, 3, 6, 6 ]))