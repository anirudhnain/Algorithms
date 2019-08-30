class Solution():
    def mutiplyTwoStrings(self,s1,s2):

        s1Arr = [int(char) for char in s1[::-1]]
        s2Arr = [int(char) for char in s2[::-1]]

        result = [0]*(len(s1)+len(s2))

        k = 0
        for num1 in s1Arr:
            carrybit = 0
            for i,num2 in enumerate(s2Arr):
                sum_temp = (result[i+k]+num1*num2+carrybit)
                result[i+k] = sum_temp%10
                carrybit = sum_temp/10
            if carrybit:
                result[i+k+1] = carrybit 
            k+=1

        skipStart = True
        ans = ''
        i = 0

        result = result[::-1]

        while i < len(result):
            while result[i]==0 and skipStart and i!=len(result)-1:
                i+=1
            skipStart = False
            ans+=str(result[i])
            i+=1
        return ans

s = Solution()
print(s.mutiplyTwoStrings("99","999"))