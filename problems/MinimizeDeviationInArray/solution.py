"""
Logic:
    To minimize the deviation we could either decrease the maximum value present in array or increase the minimum value present in array or both.
    Decrement of maximum value is only possible iff maximum value is even number.
    Increment of minimum value is only possible iff minimum value is off number.
    Now we could either try all the possible combinations of increasing the minimum value or decrease the maximum value to achieve minimum deviation OR let's make all the odd numbers even by multiplying them by 2 and then just deal with decreasing the maximum number of array until it is even.
    Since we require the maximum and minimum value of array at all the time so we could use sorted lists for better performance.

"""


import sys

from sortedcontainers import SortedList


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        sortedList = SortedList([])
        for num in nums:
            if num & 1:
                sortedList.add(num*2)
            else:
                sortedList.add(num)

        minDev = sys.maxsize
        while True:
            maxVal, minVal = sortedList[-1], sortedList[0]
            minDev = min(minDev, maxVal - minVal)
            if not maxVal & 1:
                sortedList.pop()
                sortedList.add(maxVal//2)
            else:
                break
        return minDev
