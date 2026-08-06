class Solution:
    def dp(self, grid, m, n, r, c, balance, lookup):
        if grid[r][c] == '(':
            balance += 1
        else:
            balance -= 1

        if r == m - 1 and c == n - 1:
            return balance == 0

        key = (r, c, balance)
        if key not in lookup:
            isValid = False

            for dr, dc in [[r, c + 1], [r + 1, c]]:
                if dr < m and dc < n and (balance > 0 or grid[dr][dc] == '('):
                    if self.dp(grid, m, n, dr, dc, balance, lookup) or self.dp(grid, m, n, dr, dc, balance, lookup):
                        isValid = True
                        break
            lookup[key] = isValid
        return lookup[key]

    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == ')' or grid[-1][-1] == '(' or m == n == 1:
            return False

        return self.dp(grid, m, n, 0, 0, 0, {})
