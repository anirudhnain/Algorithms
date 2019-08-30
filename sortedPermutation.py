import math
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, s):
        n = len(s)-1
        ans = 1
        arr = []
        dict_char = {}
        for char in s:
            if char in dict_char:
                dict_char[char]+=1
            else:
                dict_char[char]=1

        productOfduplicates = 1
        for key in dict_char.keys():
            productOfduplicates *= math.factorial(dict_char[key])

        for i, char in enumerate(s):
            
            arr = []
            
            for key in dict_char.keys():
                if char>key:
                    div_num = (productOfduplicates*math.factorial(dict_char[key]-1))/math.factorial(dict_char[key])
                    ans+=math.factorial(n-i)/div_num
                    
            productOfduplicates /= math.factorial(dict_char[char])
            dict_char[char]-=1
            productOfduplicates *= math.factorial(dict_char[char])
            if dict_char[char] == 0:
                del dict_char[char]
        
        return int(ans)%1000003

print (Solution().findRank("bbbbaaaa"))