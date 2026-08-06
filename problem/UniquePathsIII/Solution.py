class Solution:
    def recur(self, grid, m, n, dest, emptySquares, row, col, visited):
        if dest == (row, col):
            if emptySquares == visited-1:
                return 1
            else:
                return 0

        if grid[row][col] == -1:
            return 0

        initial = grid[row][col]
        grid[row][col] = -1
        paths = 0

        if row > 0:
            paths += self.recur(grid, m, n, dest, emptySquares, row-1, col, visited+1)
        if col > 0:
            paths += self.recur(grid, m, n, dest, emptySquares, row, col-1, visited+1)
        if row < m-1:
            paths += self.recur(grid, m, n, dest, emptySquares, row+1, col, visited+1)
        if col < n-1:
            paths += self.recur(grid, m, n, dest, emptySquares, row, col+1, visited+1)

        grid[row][col] = initial
        return paths

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dest = None
        emptySquares = 0
        startRow, startCol = None, None
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    emptySquares += 1
                elif grid[row][col] == 2:
                    dest = (row, col)
                elif grid[row][col] == 1:
                    startRow = row
                    startCol = col

        return self.recur(grid, m, n, dest, emptySquares, startRow, startCol, 0)

