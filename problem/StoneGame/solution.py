class Solution:
    def dpFn(self, piles, alex, lee, chance, lookup, i, j, result=False):
        key = (chance, alex, lee, i, j)
        if key in lookup:
            return lookup[key]
        else:
            if result:
                return result
            if i <= j:
                if chance == 1:
                    # Alex takes from front
                    alex += piles[i]
                    result = result if result else self.dpFn(piles, alex, lee, 2, lookup, i + 1, j, result)
                    # Alex takes from back
                    alex -= piles[i]
                    alex += piles[j]
                    result = result if result else self.dpFn(piles, alex, lee, 2, lookup, i, j - 1, result)
                    lookup[key] = result
                else:
                    # Lee takes from front
                    lee += piles[i]
                    result = result if result else self.dpFn(piles, alex, lee, 1, lookup, i + 1, j, result)
                    if i != j:
                        # Lee takes from back
                        lee -= piles[i]
                        lee += piles[j]
                        result = result if result else self.dpFn(piles, alex, lee, 1, lookup, i, j - 1, result)
                    lookup[key] = result
            else:
                return alex > lee
        return lookup[key]

    def stoneGame(self, piles: List[int]) -> bool:
        return self.dpFn(piles, 0, 0, 1, {}, 0, len(piles) - 1)
