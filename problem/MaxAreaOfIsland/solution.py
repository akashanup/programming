class Solution:
    def calcArea(self, grid, row, col, area, tracked):
        # Check right
        if (col < len(grid[0]) - 1) and grid[row][col + 1] == 1 and (str(row) + "#" + str(col + 1)) not in tracked:
            tracked.add((str(row) + "#" + str(col + 1)))
            area += self.calcArea(grid, row, col + 1, 1, tracked)
        # Check left
        if col > 0 and grid[row][col - 1] == 1 and (str(row) + "#" + str(col - 1)) not in tracked:
            tracked.add((str(row) + "#" + str(col - 1)))
            area += self.calcArea(grid, row, col - 1, 1, tracked)
        # Check up
        if row > 0 and grid[row - 1][col] == 1 and (str(row - 1) + "#" + str(col)) not in tracked:
            tracked.add((str(row - 1) + "#" + str(col)))
            area += self.calcArea(grid, row - 1, col, 1, tracked)
        # Check down
        if (row < len(grid) - 1) and grid[row + 1][col] == 1 and (str(row + 1) + "#" + str(col)) not in tracked:
            tracked.add((str(row + 1) + "#" + str(col)))
            area += self.calcArea(grid, row + 1, col, 1, tracked)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        tracked = set()
        for row, col in enumerate(grid):
            for key, item in enumerate(col):
                if item == 1 and (str(row) + "#" + str(key)) not in tracked:
                    tracked.add((str(row) + "#" + str(key)))
                    maxArea = max(maxArea, self.calcArea(grid, row, key, 1, tracked))
        return maxArea
