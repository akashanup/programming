class Solution:
    def dp(self, m, n, r, c, lookup):
        if r >= m or c >= n:
            return 0
        if lookup[r][c] == -1:
            if r == m-1 and c == n-1:
                lookup[r][c] = 1
            else:
                lookup[r][c] = self.dp(m, n, r+1, c, lookup) + self.dp(m, n, r, c+1, lookup)
        return lookup[r][c]

    def uniquePaths(self, m: int, n: int) -> int:
        return self.dp(m, n, 0, 0, [[-1 for _ in range(n)] for _ in range(m)])
