class Solution:
    def dp(self, grid, r, c, lookup):
        if r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 1:
            return 0
        if lookup[r][c] == -1:
            if r == len(grid)-1 and c == len(grid[0])-1:
                lookup[r][c] = 1
            else:
                lookup[r][c] = self.dp(grid, r+1, c, lookup) + self.dp(grid, r, c+1, lookup)
        return lookup[r][c]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0]:
            return 0
        return self.dp(obstacleGrid, 0, 0, [[-1 for  _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))])
