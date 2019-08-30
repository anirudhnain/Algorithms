class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        res = ""
        while A>0:
            if A%26>0:
                res=chr(A%26+ord('A')-1)+res
                A=int(A/26)
            else:
                res='Z'+res
                A=int(A/26)-1
        return res

    def titleToNumber(self, A):
        res = 0
        i=0
        for col in A[::-1]:
            res+=(ord(col)-ord('A')+1)*26**i
            i+=1
        return res

s = Solution()
print(s.titleToNumber("CV"))
print(s.convertToTitle(100))