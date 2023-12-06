import sys


class Solution:
    def maxSubArray(self, nums) -> int:
        """
            Kadane's algorithm: Kadane's algorithm is an iterative dynamic programming algorithm in which
            we search for a maximum sum contiguous subarray within a one-dimensional numeric array
        """
        maxSum = -sys.maxsize
        currSum = 0
        for num in nums:
            currSum += num
            maxSum = max(maxSum, currSum)
            currSum = max(currSum, 0)
        return maxSum


print(Solution().maxSubArray([7, -5, -2, 1, -3, 4, -1, 2, 1, -5, 4]))
