from bisect import bisect_left


class Solution:
    """
    def lis(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

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

    # Intelligently Build a Subsequence => O(n^2)
    def lis(self, nums):
        n = len(nums)
        longestSubsequence = [nums[0]]
        for i in range(1, n):
            if nums[i] > longestSubsequence[-1]:
                longestSubsequence.append(nums[i])
            else:
                j = 0
                while nums[i] > longestSubsequence[j]:
                    j += 1
                longestSubsequence[j] = nums[i]
        return len(longestSubsequence)
    """

    # Intelligently Build a Subsequence With Binary Search => O(n*Logn)
    def lis(self, nums):
        n = len(nums)
        longestSubsequence = []
        for i in range(1, n):
            j = bisect_left(longestSubsequence, nums[i])
            # If nums[i] is greater than all the elements in longestSubsequence
            if j == len(longestSubsequence):
                longestSubsequence.append(nums[i])
            # Otherwise, replace the first element in longestSubsequence greater than or equal to nums[i]
            else:
                longestSubsequence[j] = nums[i]
        return len(longestSubsequence)
