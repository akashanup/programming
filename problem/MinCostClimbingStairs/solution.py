class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = len(cost)+1
        dp = [0] * steps
        dp[0] = cost[0]
        dp[1] = cost[1]
        for step in range(2, steps):
            dp[step] = min(dp[step-1], dp[step-2])
            if step < steps - 1:
                dp[step] += cost[step]
        return dp[steps-1]
