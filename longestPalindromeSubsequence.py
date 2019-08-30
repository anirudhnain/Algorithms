class Solution(object):
    
    def __ini__(self):
        self.cache = []
    
    def palindromeRecursive(self,s, i, j):
        if j<i:
            return 0
        if self.cache[i][j]!=None:
            return self.cache[i][j]
        if (j-i)==0:
            self.cache[i][j] = 1
        elif s[i]==s[j]:
            self.cache[i][j] = self.palindromeRecursive(s,i+1,j-1)+2
        else:
            self.cache[i][j] = max(self.palindromeRecursive(s,i+1,j), self.palindromeRecursive(s,i,j-1))
        return self.cache[i][j]
    
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.cache = [[None for i in range(len(s))] for j in range(len(s))]
        return self.palindromeRecursive(s,0,len(s)-1)

s= Solution()
print(s.longestPalindromeSubseq("bbbbbbbbba"))