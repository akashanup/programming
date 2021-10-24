class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        """
            This question is similar to https://leetcode.com/problems/house-robber.
            The only difference here is that the nums is cyclic.
            So we just need to return the max of (robbing from 1st house to n-1th house, robbing from 2nd house to nth house).
            Rest, the logic remains the same.
        """

        maxAmount = 0
        for j in range(2):
            dp = [0] * (n-1)
            dp[0] = nums[j]
            dp[1] = max(nums[j], nums[j+1])
            for i in range(2, n-1):
                dp[i] = max(nums[(i+j) % n] + dp[i-2], dp[i-1])

            maxAmount = max(maxAmount, dp[-1])
        return maxAmount
