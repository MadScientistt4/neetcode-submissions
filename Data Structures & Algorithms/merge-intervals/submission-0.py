class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n, i = len(intervals), 1
        while i < n :
            print(i)
            if intervals[i-1][1] >= intervals[i][0]:
                
                start = min(intervals[i-1][0], intervals[i][0])
                end = max(intervals[i-1][1], intervals[i][1])
                new_interval = [start, end]
                
                intervals[i-1] = new_interval
                intervals.pop(i)
                i -= 1
                n -= 1
                print(i, new_interval, intervals)
            i += 1
        return intervals