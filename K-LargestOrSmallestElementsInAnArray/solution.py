import heapq


class Solution:
    def kLargestElements(self, arr, k):
        heap = [-i for i in arr]
        heapq.heapify(heap)
        largestElements = []
        for i in range(k):
            largestElements.append(-heapq.heappop(heap))
        return largestElements


print(Solution().kLargestElements([1, 23, 12, 9, 30, 2, 50], 3))


