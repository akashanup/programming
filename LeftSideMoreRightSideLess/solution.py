import sys


class Solution:
    def findPivot(self, nums):
        n = len(nums)
        pivots = [0] * n
        maxItem = -sys.maxsize
        for i in range(n):
            if nums[i] > maxItem:
                maxItem = nums[i]
                pivots[i] = 1
        minItem = sys.maxsize
        for i in range(n-1, -1, -1):
            if nums[i] < minItem:
                minItem = nums[i]
                pivots[i] = min(pivots[i], 1)
            else:
                pivots[i] = 0
        # Get index of required numbers
        i = 0
        index = 0
        while i < n:
            if pivots[i] == 0:
                pivots.pop(i)
                n -= 1
            else:
                pivots[i] = index
                i += 1
            index += 1
        return pivots
