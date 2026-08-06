class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n > 0:
            while n > 0:
                if n & 1:
                    ans *= x
                x *= x
                n >>= 1
            return ans
        else:
            n *= -1
            while n > 0:
                if n & 1:
                    ans *= x
                x *= x
                n >>= 1
            return 1 / ans
