def missingWords(s, t):
    # Write your code here
    SPACE_CHAR = " "
    missingChars = []

    i = 0
    j = 0

    word_s = ""
    word_t = ""
    moveT = True
    while i<len(s):

        if s[i] == SPACE_CHAR:
            i+=1
            continue
            
        if j<len(t) and t[j] == SPACE_CHAR and moveT:
            j+=1
            continue

        while i<len(s) and s[i]!=SPACE_CHAR:
            word_s+=s[i]
            i+=1

        while j<len(t) and t[j]!=SPACE_CHAR and moveT:
            word_t+=t[j]
            j+=1

        if word_s==word_t:
            moveT = True
            word_t = ""
        else:
            missingChars.append(word_s)
            moveT = False
        word_s = ""
    return missingChars
    
print (missingWords("I am using HackerRank to improve programming","am HackerRank to improve"))