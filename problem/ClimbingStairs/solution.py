class Solution:
    def recur(self, n, tempSum, lookup):
        if lookup[tempSum]:
            return lookup[tempSum]
        if tempSum == 0:
            lookup[tempSum] = 1
        elif tempSum < 0:
            lookup[tempSum] = 0
        else:
            lookup[tempSum] = self.recur(n, tempSum - 1, lookup) + self.recur(n, tempSum - 2, lookup)
        return lookup[tempSum]
    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        lookup = [None] * (n+1)
        return self.recur(n, n, lookup)

