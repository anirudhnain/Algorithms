class Solution():
    def wave(self, arr):

        if len(arr)<2:
            return arr
            
        arr.sort()
        
        for i in range(0,len(arr),2):
            if i+1<len(arr):
                arr[i],arr[i+1] = arr[i+1],arr[i]
            
        return arr

s = Solution()
print s.wave([10,9,8,7])