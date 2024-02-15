class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prefixSum = [0] * len(nums)
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] += prefixSum[i - 1] + nums[i]

        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < prefixSum[i - 1]:
                return nums[i] + prefixSum[i - 1]

        return -1