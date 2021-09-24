class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1:
            return intervals
        # Sort the intervals based on start time.
        intervals.sort(key=lambda x:x[0])
        i = 1
        while i < n:
            # if the start time of current interval is less that or equal to the end time of previous event then merge these two events.
            if intervals[i][0] <= intervals[i-1][1]:
                # Merge
                intervals[i-1] = [intervals[i-1][0], max(intervals[i][1], intervals[i-1][1])]
                intervals.pop(i)
                n -= 1
            else:
                i += 1
        return intervals
