class Solution:
    def dp(self, prices, fee, currentDay, holding, lookup):
        # No more stocks left
        if currentDay == len(prices):
            return 0
        if not lookup[currentDay][holding]:
            if holding:
                # Either the stocks can be held for one more day or it can be sold on current Day by giving the transaction fee.
                lookup[currentDay][holding] = max(self.dp(prices, fee, currentDay+1, holding, lookup), prices[currentDay]-fee+self.dp(prices, fee, currentDay+1, 0, lookup))
            else:
                # Either the stocks wouldn't for one more day or it could be bought on currentDay.
                lookup[currentDay][holding] = max(self.dp(prices, fee, currentDay+1, holding, lookup), -prices[currentDay]+self.dp(prices, fee, currentDay+1, 1, lookup))
        return lookup[currentDay][holding]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.dp(prices, fee, 0, 0, [[None for _ in range(2)] for _ in range(len(prices))])
