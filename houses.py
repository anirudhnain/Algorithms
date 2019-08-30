def solution(A):
    # write your code in Python 3.6
    nRows = []
    
    for elem in A:
        if not nRows:
            nRows.append(elem)
        else:
            rowFound = False
            #Optimiztion: Find row with binarySearch
            for i in range(len(nRows)):
                if elem<nRows[i]:
                    nRows[i] = elem
                    rowFound = True
                    break
            if not rowFound:
                nRows.append(elem)
    print(nRows)
    return len(nRows)

print (solution([5,7,2,6,8,2,7,6,5]))