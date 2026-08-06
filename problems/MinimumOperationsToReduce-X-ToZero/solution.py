"""
Logic:
    1. Instead of considering all the possibilities of reducing X to zero by different combinations of values of nums from start and end, we could think in reverse and find a maximum length subarray whose sum equals to sum(nums) - X.
    2. Finding this subarray is a standard problem and can be solved by using Sliding Window Technique.
"""


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        toRemove = sum(nums) - x
        if toRemove < 0: return -1

        longestSubarray = -1
        left = 0
        for right in range(N):
            toRemove -= nums[right]
            while toRemove < 0:
                toRemove += nums[left]
                left += 1
            if toRemove == 0:
                longestSubarray = max(longestSubarray, right - left + 1)

        return N - longestSubarray if longestSubarray != -1 else -1
