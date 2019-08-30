ans = []

def formCombinations(hoursLeft,daysLeft, dayHours, localString):
    if hoursLeft==0 and daysLeft==0:
        ans.append(localString)

    for i in range(dayHours+1):
        if hoursLeft-i<0 or daysLeft-1<0:
            return
        formCombinations(hoursLeft-i, daysLeft-1, dayHours, localString.replace('?', str(i), 1))

def findSchedules(workHours, dayHours, pattern):

    hoursWorked = 0
    daysLeft = 0

    for char in pattern:
        if char!='?':
            hoursWorked+=int(char)
        else:
            daysLeft+=1

    if hoursWorked == workHours:
        return [pattern]

    if hoursWorked>workHours:
        return []

    hoursLeft = workHours-hoursWorked
    formCombinations(hoursLeft,daysLeft,dayHours,pattern)
    return ans

print findSchedules(3, 2, "??2??00")