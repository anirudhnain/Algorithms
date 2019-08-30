import sys
class Solution():
    def findMedianSortedArrays(self, arr1, arr2):

        if len(arr1)>len(arr2):
            self.findMedianSortedArrays(arr2,arr1)

        x = len(arr1)
        y = len(arr2)

        low = 0
        high = x-1
        print (arr1,arr2)
        
        while low<high:

            partitionX = (low+high)>>1
            partitionY = (x+y+1)//2 - partitionX

            maxLeftX = sys.maxsize*-1 if partitionX <= 0 else arr1[partitionX-1]
            minRightX = sys.maxsize if partitionX >= x else arr1[partitionX]

            maxLeftY = sys.maxsize*-1 if ((partitionY <= 0)) else arr2[partitionY-1]
            minRightY = sys.maxsize if (partitionY >= y) else arr2[partitionY]

            if maxLeftX<=minRightY and maxLeftY<=minRightX:
                if ((x+y)%2 == 0):
                    return (min(minRightX, minRightY) + max(maxLeftX,maxLeftY))>>1
                else:
                    return max(maxLeftX,maxLeftY)
            elif maxLeftX>minRightY:
                high = partitionX
            else:
                low = partitionY+1