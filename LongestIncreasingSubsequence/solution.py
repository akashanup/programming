class Solution:
    def lis(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
    '''
    # Dynamic Programming Approach of Finding LIS by reducing the problem to longest common Subsequence
    def lis(self, nums):
        n = len(nums)
        sortedNums = sorted(list(set(nums)))
        m = len(sortedNums)
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                insertion = dp[i][j - 1]
                deletion = dp[i - 1][j]
                match = 1 + dp[i - 1][j - 1]
                if nums[i - 1] == sortedNums[j - 1]:
                    dp[i][j] = match
                else:
                    dp[i][j] = max(insertion, deletion)
        return dp[n][m]
    '''
