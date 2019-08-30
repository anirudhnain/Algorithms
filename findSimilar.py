import math
def findSimilar(a, b):
    # Write your code here
    
    hashCharCountA = {}
    hashCharCountB = {}
    
    leadingZeros = True if (a[0]=='0' or b[0]=='0') else False
    similar = True
    
    for char in a:
        if char in hashCharCountA:
            hashCharCountA[char] += 1
        else:
            hashCharCountA[char] = 1
    
    for char in b:
        if char in hashCharCountB:
            hashCharCountB[char] += 1
        else:
            hashCharCountB[char] = 1
            
    for key in hashCharCountA:
        if key not in hashCharCountB:
            similar = False
            break
        if key in hashCharCountB and hashCharCountB[key] != hashCharCountA[key]:
            similar = False
            break
            
    if leadingZeros or not similar:
        factorialProduct = 1
        subtractPositions = 0
        for key in hashCharCountB:
            if key=='0':
                subtractPositions = hashCharCountB[key]
            else:
                factorialProduct *= math.factorial(hashCharCountB[key])
        if subtractPositions>0:
            subtractPositions-=1
        ans = math.factorial(len(b)-subtractPositions)/factorialProduct
        
    else:
        factorialProduct = 1
        subtractPositions = 0
        for key in hashCharCountA:
            if key=='0':
                subtractPositions = hashCharCountA[key]
            else:
                factorialProduct *= math.factorial(hashCharCountA[key])
        if subtractPositions>0:
            subtractPositions-=1
        ans = math.factorial(len(a)-subtractPositions)/factorialProduct
    
    return int(ans)
     
print (findSimilar("1100", "1001"))