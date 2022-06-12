import sys


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start, end = 0, 0
        hashmap = {}
        maxSum = -sys.maxsize
        prefixSum = nums.copy()
        for i in range(1, len(nums)):
            prefixSum[i] += prefixSum[i - 1]
        while end < len(nums):
            if nums[end] in hashmap:
                start = max(start, hashmap[nums[end]]+1)
            hashmap[nums[end]] = end
            currSum = prefixSum[end] - prefixSum[start-1] if start > 0 else prefixSum[end]
            maxSum = max(maxSum, currSum)
            end += 1
        return maxSum
