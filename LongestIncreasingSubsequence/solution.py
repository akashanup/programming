class Solution:
    def lis(self, nums):
        n = len(nums)
        dp = {}
        for i in range(n-1, -1, -1):
            dp[nums[i]] = 1
            for j in range(i, n - 1):
                if nums[j] <= nums[j + 1]:
                    if (j + 1) in dp:
                        dp[nums[i]] = dp[nums[i]] + dp[j + 1]
                        break
                    dp[nums[i]] = dp[nums[i]] + 1
        return max(dp.values())
    '''
    # Dynamic Programming Approach of Finding LIS by reducing the problem to longest common Subsequence
    def lis(self, nums):
        n = len(nums)
        sortedNums = sorted(nums)
        dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                insertion = dp[i][j - 1]
                deletion = dp[i - 1][j]
                match = 1 + dp[i - 1][j - 1]
                mismatch = dp[i - 1][j - 1]
                if nums[i - 1] == sortedNums[j - 1]:
                    dp[i][j] = max(insertion, deletion, match)
                else:
                    dp[i][j] = max(insertion, deletion, mismatch)
        return dp[n][n]
    '''
