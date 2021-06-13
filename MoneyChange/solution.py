import sys


class Solution:
    def dpFn(self, m, coins, lookup):
        if lookup[m] is None:
            if m == 0:
                lookup[m] = 0
            elif m < 0:
                lookup[m] = sys.maxsize
            else:
                minCoins = sys.maxsize
                for i in coins:
                    if m >= i:
                        minCoins = min(minCoins, 1 + self.dpFn(m - i, coins, lookup))
                lookup[m] = minCoins
        return lookup[m]

    def getChange(self, m, coins):
        return self.dpFn(m, coins, [None] * (m + 1))
