class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Flip rows if first element is 0 because 1 at first index will always give a greater number. For example, 1000...000 will always be greater than 0111...111
        for row in range(m):
            if grid[row][0] == 0:
                grid[row] = [1 if num == 0 else 0 for num in grid[row]]

        # Flip columns if count of zeros is greater than count of ones. This can be assumed to be always making the greater number than before because we are not changing anything for first column.
        for j in range(1, n):
            zeros = 0
            for i in range(m):
                if grid[i][j] == 0:
                    zeros += 1
            if zeros > m-zeros:
                for i in range(m):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0

        maxSum = 0
        for row in grid:
            maxSum += int(''.join([str(_) for _ in row]), 2)

        return maxSum
