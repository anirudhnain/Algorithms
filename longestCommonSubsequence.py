class Solution(object):
    
    def __ini__(self):
        self.cache = []
    
    def longestCommonRecursive(self,s, t, i, j):
        if i == len(s) or j==len(t):
            return 0
        if self.cache[i][j]!=None:
            return self.cache[i][j]
        if s[i]==t[j]:
            self.cache[i][j] = self.longestCommonRecursive(s, t, i+1,j+1)+1
        else:
            self.cache[i][j] = max(self.longestCommonRecursive(s,t,i+1,j), self.longestCommonRecursive(s,t,i,j+1))
        return self.cache[i][j]
    
    def longestCommonSubseq(self, s, t):
        """
        :type s: str
        :rtype: int
        """
        self.cache = [[None for i in range(len(t))] for j in range(len(s))]
        ans = self.longestCommonRecursive(s,t,0,0)
        return ans

s = Solution()
print(s.longestCommonSubseq("AGGTAB", "GXTXAYB"))