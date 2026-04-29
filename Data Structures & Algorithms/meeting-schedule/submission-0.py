"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sort_intervals = sorted(intervals,  key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if sort_intervals[i].start < sort_intervals[i-1].end:
                return False
        return True