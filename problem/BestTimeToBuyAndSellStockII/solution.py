import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp = [[None for j in range(2)] for i in range(days+1)]

        dp[0][0] = 0
        dp[0][1] = -sys.maxsize

        for i in range(1, days+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i-1])

        return dp[-1][0]
