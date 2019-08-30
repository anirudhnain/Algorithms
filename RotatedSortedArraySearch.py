class Solution:

    def binarySearch(self, A, lo, hi, B):
        while lo<hi:
            mi = (lo+hi)>>1
            if A[mi] == B:
                return mi
            elif A[mi]<B:
                lo = mi+1
            else:
                hi = mi

    def pivotPoint(self, A):
        lo = 0
        hi = len(A)
        
        while lo<hi:
            mi = (lo+hi)>>1
            if mi>0 and mi<len(A)-1 and A[mi-1]<A[mi]>A[mi+1]:
                return mi
            elif mi==0 and A[mi]>A[mi+1]:
                return 0
            elif mi==len(A)-1 and A[mi-1]>A[mi]:
                return mi-1
            elif mi<len(A)-1 and A[mi]<A[mi+1] and A[mi]>A[0]:
                lo = mi+1
            else:
                hi = mi
        return lo

    def findElem(self,A, T):
        pivotIndex = self.pivotPoint(A)
        searchA = self.binarySearch(A, 0, pivotIndex+1, T)
        searchB = self.binarySearch(A, pivotIndex, len(A), T)
        
        if searchA!=None:
            return searchA
        if searchB!=None:
            return searchB
        return -1

s = Solution()
print(s.findElem([ 1, 7, 67, 133, 178 ], 1))