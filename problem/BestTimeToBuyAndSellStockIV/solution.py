import sys

"""
Logic:
This problem can be solved using dynamic programming.
Let create a dp array (dp[i][k][a])in which the i-th position will tell the maximum profit at the end of i-th day with 
at most k transaction.
dp[i][k][a], i denotes the day, k denotes the maximum number of allowed transactions and a denotes whether we have sold 
or buys the stocks at the end of the ith day. For example,
dp[i][k][0] will tell the maximum profit at i-th day with at most k transaction such that on i-th day we have sold the 
stocks.
dp[i][k][1] will tell the maximum profit at i-th day with at most k transaction such that on i-th day we have bought the 
stocks.
Base cases:
dp[0][k][0] = 0 => because on 0th day we don't have any stock.
dp[0][k][1] = -infinity => since we don't have any stocks on 0th day so we can't buy any stock
dp[i][0][0] = 0 => because the number of transactions is 0 so profit is 0
dp[i][0][1] = -infinity => since the number of transactions is 0 so we can't buy any stock
DP state:
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i-1])
Since a is 0 which means the action taken on ith day is either Rest* or Sell. Therefore the max profit would be the 
max of Rest action(dp[i-1][k][0]) and Sell action(dp[i-1][k][1]+prices[i-1]). Note: To sell a stock we must have 
bought a stock before.
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i-1])
Since a is 1 which means the action taken on ith day is either Rest* or Buy. Therefore the max profit would be the 
max of Rest action(dp[i-1][x][1]) and Buy action(dp[i-1][k-1][0]-prices[i-1]).
At last, we have to return dp[-1][k][0] because if we don't hold any stock at the end then only we can have the maximum 
profit.
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
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
        
        return dp[-1][k][0]
