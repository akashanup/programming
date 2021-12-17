class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days, k = len(prices), 1
        dp = [[[None for _ in range(2)] for _ in range(k+1)] for _ in range(days+1)]

        for x in range(k+1):
            dp[0][x][0] = 0
            dp[0][x][1] = -sys.maxsize

        for i in range(1, days+1):
            dp[i][0][0] = 0
            dp[i][0][1] = -sys.maxsize
            for x in range(1, k+1):
                dp[i][x][0] = max(dp[i-1][x][0], dp[i-1][x][1]+prices[i-1])
                dp[i][x][1] = max(dp[i-1][x][1], dp[i-1][x-1][0]-prices[i-1])

        return dp[-1][1][0]
