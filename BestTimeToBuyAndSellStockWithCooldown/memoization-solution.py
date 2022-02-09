class Solution:
    def dp(self, prices, currentDay, holding, lookup):
        # Return 0 if there are no more stocks.
        if currentDay >= len(prices):
            return 0
        if not lookup[currentDay][holding]:
            if holding:
                # Return max(did nothing on current day, sold all the stocks on current day and moved to next date after cooldown day).
                lookup[currentDay][holding] = max(self.dp(prices, currentDay+1, holding, lookup), prices[currentDay] + self.dp(prices, currentDay+2, 0, lookup))
            else:
                # Return max(did nothing on current day, bought all the stocks on current day).
                lookup[currentDay][holding] = max(self.dp(prices, currentDay+1, holding, lookup), -prices[currentDay] + self.dp(prices, currentDay+1, 1, lookup))
        return lookup[currentDay][holding]

    def maxProfit(self, prices: List[int]) -> int:
        return self.dp(prices, 0, 0, [[None for _ in range(2)] for _ in range(len(prices))])

