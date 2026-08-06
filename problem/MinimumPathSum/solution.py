import sys


class Solution:
    def dpFn(self, grid, m, n, minSum, lookup):
        if lookup[m][n] is not None:
            return lookup[m][n]

        if m == 0 and n == 0:
            return grid[m][n]

        tempMinSum = sys.maxsize

        if m > 0 and n > 0:
            tempMinSum = min(tempMinSum, grid[m][n] + min(self.dpFn(grid, m - 1, n, minSum, lookup),
                                                          self.dpFn(grid, m, n - 1, minSum, lookup)))
        elif m > 0:
            tempMinSum = min(tempMinSum, grid[m][n] + self.dpFn(grid, m - 1, n, minSum, lookup))
        else:
            tempMinSum = min(tempMinSum, grid[m][n] + self.dpFn(grid, m, n - 1, minSum, lookup))
        lookup[m][n] = min(tempMinSum, minSum)
        return lookup[m][n]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        lookup = [[None for _ in range(n)] for _ in range(m)]
        return self.dpFn(grid, m - 1, n - 1, sys.maxsize, lookup)
