class Solution:
    def maxSubArray(self, nums) -> int:
        """
            Kadane's algorithm: Kadane's algorithm is an iterative dynamic programming algorithm in which we search for a maximum sum contiguous subarray within a one-dimensional numeric array
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)


print(Solution().maxSubArray([7, -5, -2, 1, -3, 4, -1, 2, 1, -5, 4]))
