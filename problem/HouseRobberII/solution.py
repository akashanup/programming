class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        if houses <= 3:
            return max(houses)

        """
            This question is similar to https://leetcode.com/problems/house-robber.
            The only difference here is that the nums is cyclic.
            So we just need to return the max of (robbing from 0th house to n-1th house, robbing from 1st house to nth house).
            Rest, the logic remains the same.
        """

        # Dp for houses[:-1]
        dp = [None] * (houses-1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for house in range(2, houses-1):
            dp[house] = max(nums[house]+dp[house-2], dp[house-1])

        maxLoot = dp[-1]

        # Dp for houses[1:]
        dp = [None] * houses
        dp[0] = 0
        dp[1] = nums[1]
        for house in range(2, houses):
            dp[house] = max(nums[house]+dp[house-2], dp[house-1])

        return max(maxLoot, dp[-1])

