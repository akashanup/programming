class Solution:
    def longestPalindromeSubseq(self, s: str, lookup={}) -> int:
        dp = [[0 for _ in range(len(s))]  for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1

        for x in range(2, len(s)+1):
            for i in range(len(s)-x+1):
                j = i+x-1
                if s[i] == s[j] and x == 2:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j]);

        return dp[0][-1]
