import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        hashmap = {}
        # O(n)
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1

        data = [(count, num) for num, count in hashmap.items()]

        heap = []
        # O(KlogK)
        for i in range(k):
            heapq.heappush(heap, data[i])

        # O((N-K)logK)
        for i in range(k, len(data)):
            count, num = data[i]
            if heap[0][0] < count:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, num))

        frequent = [None] * k
        for i in range(k):
            frequent[i] = heapq.heappop(heap)[1]

        return frequent
