class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    previousPairsCount = (dp[i - 1][j] + ((10**9) + 7) - (dp[i - 1][j - i] if (j - i) >= 0 else 0)) % ((10**9) + 7)
                    dp[i][j] = (dp[i][j - 1] + previousPairsCount) % ((10**9) + 7)
        return (dp[n][k] + ((10**9) + 7) - (dp[n][k - 1] if k > 0 else 0)) % ((10**9) + 7)
