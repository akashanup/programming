class Solution:
    def longestPalindrome(self, s: str) -> str:
        s1 = s[::-1]
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(s) + 1):
                insertion = dp[i][j-1]
                deletion = dp[i-1][j]
                match = 1 + dp[i-1][j-1]
                mismatch = dp[i-1][j-1]
                if s[i-1] == s1[j-1]:
                    dp[i][j] = max(insertion, deletion, match)
                else:
                    dp[i][j] = max(insertion, deletion, mismatch)
        return dp[len(s)][len(s)]


print(Solution().longestPalindrome("abcdcbaabcd"))
