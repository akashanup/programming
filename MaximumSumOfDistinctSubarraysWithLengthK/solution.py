class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0] * len(nums)
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        lookup = {}
        maxSum = 0
        currSum = 0
        i, j = 0, 0
        while j < len(nums):
            if nums[j] in lookup and lookup[nums[j]] >= i:
                i = lookup[nums[j]] + 1
                currSum = prefixSum[j-1] - prefixSum[lookup[nums[j]]]
            currSum += nums[j]
            lookup[nums[j]] = j
            if j-i+1 == k:
                maxSum = max(maxSum, currSum)
                currSum -= nums[i]
                i += 1
            j += 1
        return maxSum
