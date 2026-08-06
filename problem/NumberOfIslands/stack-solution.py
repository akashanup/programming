class Solution:
    DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def dfs(self, grid, m, n, row, col):
        for direction in Solution.DIRECTIONS:
            newRow = row + direction[0]
            newCol = col + direction[1]
            # Recur for all its neighbours having "1" and mark them as visited
            if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == "1":
                grid[newRow][newCol] = "0"
                # Recur
                self.dfs(grid, m, n, newRow, newCol)

    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        island = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    # Mark it visited
                    grid[row][col] = "0"
                    island += 1
                    self.dfs(grid, m, n, row, col)
        return island


grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]
print(Solution().numIslands(grid))
