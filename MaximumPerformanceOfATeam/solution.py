import heapq


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        employees = [[speed[i], efficiency[i]] for i in range(n)]
        employees.sort(key=lambda employee: employee[1], reverse=True)
        maxPerformanceTeamSpeed = []
        heapq.heapify(maxPerformanceTeamSpeed)
        totalTeamSpeed = 0
        maxPerformanceScore = 0
        for i in range(n):
            heapq.heappush(maxPerformanceTeamSpeed, employees[i][0])
            if i < k:
                totalTeamSpeed += employees[i][0]
            else:
                totalTeamSpeed += employees[i][0] - heapq.heappop(maxPerformanceTeamSpeed)
            maxPerformanceScore = max(maxPerformanceScore, totalTeamSpeed * employees[i][1])
        return maxPerformanceScore % ((10**9) + 7)
