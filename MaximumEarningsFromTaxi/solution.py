import heapq


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[0])
        heap = []
        maxProfit = 0
        currentProfit = 0
        for ride in rides:
            while heap and heap[0][0] <= ride[0]:
                _, tempProfit = heapq.heappop(heap)
                currentProfit = max(currentProfit, tempProfit)
            heapq.heappush(heap, [ride[1], currentProfit + ride[1] - ride[0] + ride[2]])
            maxProfit = max(maxProfit, currentProfit + ride[1] - ride[0] + ride[2])
        return maxProfit
