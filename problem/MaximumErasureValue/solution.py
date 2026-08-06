class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxSum = 0
        tempMaxSum = 0
        lookup = {}
        i = 0
        for key, value in enumerate(nums):
            if value in lookup:
                while i <= lookup[value]:
                    tempMaxSum -= nums[i]
                    i += 1
            lookup[value] = key
            tempMaxSum += value
            maxSum = max(maxSum, tempMaxSum)
        return maxSum
