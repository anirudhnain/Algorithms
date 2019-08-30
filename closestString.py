class Solution:
    def closestString(self, arr, str1, str2):
        indexElem1 = None
        indexElem2 = None
        ans = len(arr)
        for i,elem in enumerate(arr):
            if elem == str1:
                indexElem1=i
            if elem == str2:
                indexElem2 = i
            if indexElem1!=None and indexElem2!=None:
                ans = min(abs(indexElem1-indexElem2),ans)
        return ans
s = Solution()
print(s.closestString(["li","ab","cd"],"ab","li"))