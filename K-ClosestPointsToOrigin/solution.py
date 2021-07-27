class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points

        import heapq
        closestPoints = []
        heapq.heapify(closestPoints)

        for point in points:
            heapq.heappush(closestPoints, (point[0] ** 2 + point[1] ** 2, point))

        return [heapq.heappop(closestPoints)[1] for _ in range(k)]
