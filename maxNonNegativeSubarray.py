class Solution:
    # @param A : list of integers
    # @return a list of integers

    def findAns(self, temp_array, ans):
        if sum(temp_array)>sum(ans):
            return temp_array
        if sum(temp_array) == sum(ans):
            if len(temp_array) > len(ans):
                return temp_array
            elif temp_array > ans:
                return temp_array
        return ans

    def maxset(self, A):
        ans = []
        temp_array = []
        for elem in A:
            if elem>=0:
                temp_array.append(elem)
            else:
                if temp_array:
                    ans = self.findAns(temp_array, ans)
                temp_array = []

        if temp_array:
            ans = self.findAns(temp_array, ans)
        
        return ans
s = Solution()
print s.maxset([ 0, 0, -1, 0 ])