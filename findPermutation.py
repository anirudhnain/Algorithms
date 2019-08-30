class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        if A==0:
            return []

        ans = [1]
            
        decreasingSequence = 0
        for i in range(len(B)):
            char = B[i]
            if (char=='I'):
                ans.append(i+2)
                decreasingSequence = 0
            else:
                decreasingSequence+=1
                if i == len(B)-1 or B[i+1] == 'I':
                    number = ans.pop()
                    for i in range(number+decreasingSequence,number,-1):
                        ans.append(i)
                    ans.append(number)
        return ans        

s = Solution()
print (s.findPerm(4,"IDDIDD"))