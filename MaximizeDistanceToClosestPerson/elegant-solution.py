class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        startIndex = 0
        maxConsecutiveZeros = 0
        for currentIndex, seat in enumerate(seats):
            if seat:
                if seats[startIndex]:
                    maxConsecutiveZeros = max(maxConsecutiveZeros, (currentIndex - startIndex) // 2)
                else:
                    maxConsecutiveZeros = max(maxConsecutiveZeros, (currentIndex - startIndex))
                startIndex = currentIndex

        if seats[startIndex]:
            maxConsecutiveZeros = max(maxConsecutiveZeros, len(seats) - 1 - startIndex)

        return maxConsecutiveZeros
