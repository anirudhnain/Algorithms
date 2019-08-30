months_map = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
def compareDates(date1, date2):
    date1Arr = date1.split(' ')
    date2Arr = date2.split(' ')
    
    if int(date1Arr[-1])>int(date2Arr[-1]):
        return 1
    elif int(date2Arr[-1])>int(date1Arr[-1]):
        return -1
    elif months_map[date1Arr[1]] > months_map[date2Arr[1]]:
        return 1
    elif months_map[date2Arr[1]] > months_map[date1Arr[1]]:
        return -1
    elif date1Arr[0]>date2Arr[0]:
        return 1
    elif date2Arr[0]>date1Arr[0]:
        return -1
    return 0

def sortDates(dates):
    # Write your code here    
    dates.sort(compareDates)
    return dates

print (sortDates(["20 Oct 2052","06 Jun 1933","26 May 1960","20 Sep 1958","16 Mar 2068","25 May 1912","16 Dec 2018","26 Dec 2061","04 Nov 2030","28 Jul 1963"]))