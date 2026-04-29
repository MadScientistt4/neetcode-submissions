"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        arr = [intervals[0].end]
        conflict, flag = 1, 0
        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                n = len(arr)
                flag = 0
                for j in range(n):
                    if arr[j] <= intervals[i].start:
                        arr[j] = intervals[i].end
                        flag = 1
                        
                        break
                if flag != 1:
                    conflict += 1
                    arr.append(intervals[i].end)
                print(arr)   
                    
        return conflict


                        


                