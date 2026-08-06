"""
import sys


class Solution:
    def dp(self, nums, k, index, lookup):
        if lookup[index] is not None:
            return lookup[index]
        if index == 0:
            return nums[0]
        maxScore = -sys.maxsize
        for i in range(1, k + 1):
            if index - i >= 0:
                maxScore = max(maxScore, nums[index] + self.dp(nums, k, index - i, lookup))
        lookup[index] = maxScore
        return lookup[index]

    def maxResult(self, nums, k: int) -> int:
        lookup = [None] * (len(nums) + 1)
        self.dp(nums, k, len(nums) - 1, lookup)
        return lookup[len(nums) - 1]
"""

from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        deq = deque([n-1])
        print(n, nums)
        for i in range(n-2, -1, -1):
            if deq[0] - i > k:
                deq.popleft()
            nums[i] += nums[deq[0]]
            while len(deq) and nums[deq[-1]] <= nums[i]:
                deq.pop()
            deq.append(i)
        return nums[0]


print(Solution().maxResult(nums=[1, -1, -2, 4, -7, 3], k=2))
print(Solution().maxResult(nums=[10, -5, -2, 4, 0, 3], k=3))
print(Solution().maxResult(nums=[1, -5, -20, 4, -1, 3, -6, -3], k=2))
