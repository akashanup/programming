import sys


class Solution:
    """
        Consider the numbers are in range 1-n.
        We need to check for all numbers from 1 to n for which the total penalty is minimum.
        Suppose we guessed a number k between 1-n, therefore, our penalty would be =>
            k + max(penalty for numbers in the range 1 to k-1, penalty for numbers in the range k+1 to n)
            as after every guess we would know when the target is lower than or greater than our guess.
        Now we just need to find the penalty for all k in the range 1-n and the k which gives the minimum penalty would be our answer.
    """
    def dp(self, start, end, lookup):
        if start >= end:
            return 0
        if (start, end) not in lookup:
            money = sys.maxsize
            for penalty in range(start, end+1):
                money = min(money, penalty + max(self.dp(start, penalty - 1, lookup), self.dp(penalty+1, end, lookup)))
            lookup[(start, end)] = money
        return lookup[(start, end)]

    def getMoneyAmount(self, n: int) -> int:
        return self.dp(1, n, {})

