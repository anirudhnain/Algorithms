class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        intervals.sort(key=lambda x: x.start)

        if len(intevals)<1:
        	return []

        new_interval = [intervals[0]]

        for i in range(1, len(intervals)):
        	current_elem = intevals[i]
        	new_interval_elem = new_interval[-1]

        	if new_interval_elem.end<current_elem.start:
        		new_interval.append(current_elem)
        	else:
        		new_interval[-1].start = min(new_interval_elem.start, current_elem.start)
        		new_interval[-1].end = max(new_interval_elem.end, current_elem.end)

        return new_interval


intevals = []
intevals.append(Interval(1,3))
intevals.append(Interval(2,6))
intevals.append(Interval(8,10))
intevals.append(Interval(15,18))

s = Solution()
new_interval =  s.merge(intevals)

for elem in new_interval:
	print elem.start,elem.end
        