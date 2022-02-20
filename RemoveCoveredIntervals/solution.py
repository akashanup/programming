class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        count = len(intervals)
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            if start <= intervals[i][0] and intervals[i][1] <= end:
                count -= 1
            else:
                start, end = intervals[i][0], intervals[i][1]
        return count
