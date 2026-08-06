"""Logic:
Create a dp matrix of rows as coins and columns as price from 0 to amount.
    dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
Base case:
    To get amount zero, we will have only one way for each coins and that is to reject that coin.
        for i in range(len(coins)): dp[i][0] = 1
Now loop for each coin for each price from 1, amount:
    If the value of current coin is more than the current price then certainly this coin can't be taken. So the value of dp for current coin and current price will be same as the dp value of previous coin and current price.
        if coins[i] > j: dp[i][j] = dp[i-1][j]
    Else, the value of dp for current coin and current price will be the dp value of previous coin and current price + the dp value of current coin with (current price - current coin)
        else: dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
    At last, return the last value of dp.
        return dp[-1][-1]
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        
        for i in range(len(coins)):
            dp[i][0] = 1
            
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if coins[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
        return dp[-1][-1]
