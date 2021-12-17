import sys

"""
Logic:
This problem can be solved using dynamic programming.
Let create a dp array (dp[i][k][a])in which the i-th position will tell the maximum profit at the end of i-th day with atmost k transaction.
dp[i][a], i denotes the day and a denotes whether we have sold or buyes the stocks at the end of the ith day. For example,
dp[i][0] will tell the maximum profit at i-th day such that on i-th day we have sold the stocks.
dp[i][1] will tell the maximum profit at i-th day such that on i-th day we have bought the stocks.
Base cases:
dp[0][0] = 0 => because on 0th day we don't have any stock.
dp[0][1] = -infinity => since we don't have any stocks on 0th day so we can't buy any stock
DP state:
dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
Since a is 0 which means the action taken on ith day is either Rest* or Sell. Therefore the max profit would be the max of Rest action(dp[i-1][0]) and Sell action(dp[i-1][1]+prices[i-1]). Note: To sell a stock we must have buyed a stock before.
dp[i][1] =
When i == 1: max(dp[i-1][1], -prices[i-1]) Since we can't buy a stock on ith day untill and unless it is sold on i-2th day
When i > 1: max(dp[i-1][1], dp[i-2][0]-prices[i-1])
Since a is 1 which means the action taken on ith day is either Rest* or Buy. Therefore the max profit would be the max of Rest action(dp[i-1][1]) and Buy action(dp[i-1][0]-prices[i-1]).
At last, we have to return dp[-1][0] because if we don't hold any stock at the end then only we can have the maximum profit.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp = [[None for j in range(2)] for i in range(days+1)]
        
        dp[0][0] = 0
        dp[0][1] = -sys.maxsize
        
        for i in range(1, days+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            if i == 1:
                dp[i][1] = max(dp[i-1][1], -prices[i-1])
            else:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i-1])
        
        return dp[-1][0]
