class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervalsLen = len(intervals)
        if intervalsLen == 0:
            return 0

        # Sort on the basis of end first then on start if the end is same for any interval.
        intervals.sort(key=lambda x: (x[1], x[0]))

        """
            Since the elements are sorted on the basis of end, we just need to check whether the next interval overlaps with current.
            Now iterate over the intervals and perform the below steps-
            1. If the next interval overlaps, then erase the next interval and move to next of next interval.
            2. Else move forward.
        """
        left, right, erased = 0, 1, 0
        while right < intervalsLen:
            if intervals[left][1] > intervals[right][0]:
                erased += 1
            else:
                left = right
            right += 1

        return erased
