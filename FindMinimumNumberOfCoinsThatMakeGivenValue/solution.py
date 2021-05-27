class Solution:
    def applicableCombinations(self, coins, val, lasCoinUsed, combination):
        if val == 0:
            return combination
        else:
            for i in coins[coins.index(lasCoinUsed):]:
                if val - i >= 0:
                    combination.append(i)
                    return self.applicableCombinations(coins, val - i, i, combination)
            return []

    def minCoins(self, coins, val):
        coins = sorted(coins, reverse=True)
        combinations = []
        for i in coins:
            combination = self.applicableCombinations(coins, val, i, [])
            if len(combination):
                combinations.append(combination)
        print(combinations)
        if len(combinations):
            combinations.sort(key=lambda x: len(x))
            return len(combinations[0])
        else:
            return -1
