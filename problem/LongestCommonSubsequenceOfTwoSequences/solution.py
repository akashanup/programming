class Solution:
    def constructAlignment(self, a, b, dp):
        alignment = ""
        found = False
        for i in range(len(dp) - 1, 0, -1):
            for j in range(len(dp[0]) - 1, 0, -1):
                if dp[i][j] != max(dp[i-1][j], dp[i][j-1]):
                    alignment = a[i-1] + alignment  # Or alignment += b[j]
                    if len(alignment) == dp[-1][-1]:
                        found = True
                        break
            if found is True:
                break
        return alignment

    def lcs(self, a, b):
        lenA = len(a)
        lenB = len(b)
        dp = [[0 for i in range(lenB + 1)] for j in range(lenA + 1)]
        for i in range(1, lenA + 1):
            for j in range(1, lenB + 1):
                insertion = dp[i][j - 1]
                deletion = dp[i - 1][j]
                match = dp[i - 1][j - 1] + 1
                mismatch = dp[i - 1][j - 1]
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = max(insertion, deletion, match)
                else:
                    dp[i][j] = max(insertion, deletion, mismatch)
        print(self.constructAlignment(a, b, dp))
        return dp[lenA][lenB]


print(Solution().lcs("stone", "longest"))
print(Solution().lcs("edit", "distance"))
