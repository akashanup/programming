class Solution:
    def dp(self, coins, amount, index, lookup):
        if amount == 0:
            return 1
        if lookup[index][amount] == -1:
            combinations = 0
            for i in range(index, len(coins)):
                if amount >= coins[i]:
                    combinations += self.dp(coins, amount-coins[i], i, lookup)
            lookup[index][amount] = combinations
        return lookup[index][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        return self.dp(coins, amount, 0, [[-1 for _ in range(amount+1)] for _ in range(len(coins))])
