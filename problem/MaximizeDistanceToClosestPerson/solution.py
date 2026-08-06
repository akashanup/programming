import math


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxContinuousZeros = 0
        continuousZeros = 0
        for person in seats:
            if person:
                maxContinuousZeros = max(maxContinuousZeros, continuousZeros)
                continuousZeros = 0
            else:
                continuousZeros += 1
        maxContinuousZeros = max(maxContinuousZeros, continuousZeros)
        maxContinuousZeros = math.ceil(maxContinuousZeros / 2)

        # Check if max zeros are from start or end
        continuousZerosFromStart = 0
        continuousZerosFromEnd = 0
        start = 0
        end = len(seats)-1
        while not seats[start] or not seats[end]:
            if not seats[start]:
                continuousZerosFromStart += 1
                start += 1
            if not seats[end]:
                continuousZerosFromEnd += 1
                end -= 1
        if continuousZerosFromStart >= maxContinuousZeros or continuousZerosFromEnd >= maxContinuousZeros:
            return max(continuousZerosFromStart, continuousZerosFromEnd)

        return maxContinuousZeros
