class Solution:
    def solve(self, A, B, C):

        maxSizeBNumberString = ''.join(['9' for i in range(B)])

        minNumber = min(int(maxSizeBNumberString),C)
        minString = str(minNumber)

        ans=0

        if(len(minString) < B):
            return 0

        array = []

        for i in range(len(minString)):
            if i!=0 and not array:
                break
            if array:
                array.pop(0)
            char = int(minString[i])

            for elem in A:
                if elem<char:
                    if (i==0 and elem==0 and B!=1):
                        continue
                    ans+=(len(A))**(len(minString)-1-i)
                if elem == char and minNumber==C:
                    array.append(elem)
                    print array
                elif elem == char:
                    ans+=(len(A))**(len(minString)-1-i)
        return ans

s = Solution()
print s.solve( [ 0, 2, 6, 8, 9 ], 1, 1278)