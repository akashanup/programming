class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0]:
            return 0
        dp = [[0 for  _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        dp[0][0] = 1
        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 0:
                    if r > 0:
                        dp[r][c] += dp[r-1][c]
                    if c > 0:
                        dp[r][c] += dp[r][c-1]
        return dp[-1][-1]
