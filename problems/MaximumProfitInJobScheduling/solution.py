import heapq


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))], key=lambda x: x[0])
        heap = []
        currentProfit = 0
        maxProfit = 0
        for start, end, profit in jobs:
            # Calculate the total profit of all the jobs that would have end by this time(start: startTime of current job)
            while heap and heap[0][0] <= start:
                _, tempProfit = heapq.heappop(heap)
                currentProfit = max(currentProfit, tempProfit)

            # Push the job into heap to use it further. It's profit would be definitely currentProfit + profit(of current job)
            heapq.heappush(heap, (end, currentProfit + profit))
            maxProfit = max(maxProfit, currentProfit + profit)

        return maxProfit
