class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n, largestSquareLength = len(matrix), len(matrix[0]), 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    largestSquareLength = max(largestSquareLength, dp[i][j])

        return largestSquareLength * largestSquareLength
