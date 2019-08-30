def threeSum(A, target):

    A_frequency = {}

    for elem in A:
        if elem in A_frequency:
            A_frequency[elem]+=1
        else:
            A_frequency[elem] = 1

    print (A_frequency)

    n = len(A)
    i = 0
    r = len(A)-1
    A.sort()
    print (A)
    res = 0
    for i in range(len(A)):
        fixedValue = A[i]
        sumLeft = target-A[i]
        A_frequency[fixedValue]-=1
        processed = set()
        for j in range(i+1,len(A)):
            twoSumPair1 = A[j]
            twoSumPair2 = sumLeft-A[j]
            pair = tuple(sorted([twoSumPair1,twoSumPair2]))
            if pair in processed:
                continue
            if twoSumPair2 in A_frequency:
                if twoSumPair1 == twoSumPair2:
                    res+=((A_frequency[twoSumPair2]-1)*(A_frequency[twoSumPair1]-2))/2
                else:
                    res+=A_frequency[twoSumPair2]*A_frequency[twoSumPair1]
                processed.add(pair)
        print (fixedValue, processed,res)
    return res

# n = int(input())
# skills = [int(x) for x in input().split()]
# target = int(input())

print(threeSum([1,1,1,1],3))