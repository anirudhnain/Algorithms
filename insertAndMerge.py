class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        
        
        if len(intervals)<1:
            return []
        
        n = len(intervals)
        
        for i in range(0, n):
            if new_interval.start<=intervals[i].start:
                intervals.insert(i, new_interval)
                break
            elif i==n-1:
                intervals.append(new_interval)

        new_intervals = [intervals[0]]
        
        for i in range(1, n+1):
            current_elem = intervals[i]
            new_interval_elem = new_intervals[-1]

            if new_interval_elem.end<current_elem.start:
                new_intervals.append(current_elem)
            else:
                new_intervals[-1].start = min(new_interval_elem.start, current_elem.start)
                new_intervals[-1].end = max(new_interval_elem.end, current_elem.end)

        return new_intervals

intevals = []
intevals.append(Interval(5735878, 14055448))

s = Solution()
new_interval =  s.insert(intevals, Interval(45639660, 84793834))

for elem in new_interval:
    print elem.start,elem.end
        