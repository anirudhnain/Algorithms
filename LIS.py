class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        arr = [[1,1] for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i]>nums[j]:
                    prev_val = arr[i][0]
                    arr[i][0] = max(arr[i][0], arr[j][0]+1)
                    if arr[i][0]>prev_val:
                        arr[i][1] = arr[j][1]
                    elif arr[i][0] == arr[j][0]+1:
                        arr[i][1] += arr[j][1]

        max_len = -1
        for elem in arr:
            max_len = max(max_len, elem[0])
        
        ans = 0

        for elem in arr:
            if elem[0] == max_len:
                ans+=elem[1]

        return ans

s = Solution()
print s.findNumberOfLIS([5,5,5])