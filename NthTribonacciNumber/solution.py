class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        a, b, c = 0, 1, 1
        for i in range(3, n+1):
            a, b, c = b, c, a+b+c
        return c
        """
            if n == 0:
                return 0
            if n <= 2:
                return 1
            t = [0] * (n+1)
            t[0] = 0
            t[1] = 1
            t[2] = 1
            for i in range(3, n+1):
                t[i] = t[i-1] + t[i-2] + t[i-3]
            return t[n]
        """
