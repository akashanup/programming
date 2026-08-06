class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
            This question is similar to https://leetcode.com/problems/house-robber.
            The only difference here is we need to first calculate the money in each house.
            Let us consider, we have houses from 0 to max(nums). Now each time a number occurs in nums, we add that number to its corresponding house.
            At the end we will left with houses and the money they have.
            
        """
        lookup = [0] * (max(nums) + 1)
        for num in nums:
            lookup[num] += 1

        n = len(lookup)
        dp = [0] * n
        dp[0] = lookup[0]
        dp[1] = max(lookup[0], lookup[1])
        for i in range(2, n):
            dp[i] = max(i*lookup[i] + dp[i-2], dp[i-1])
        return dp[-1]
