"""
1. Iterating the input A backward, then for each A[i], find how many round it can remove on its right.
2. dp[i] means the number of element A[i] can eat on its right.
3. More precisely, the number of rounds for an element A[i], to completely remove whatever it can eat on the right of A[i], if it is possible.
4. Iterative input array A reversely,
    i. If A[i] is bigger the last element A[j] of stack, this means A[i] can remove that element,
    ii. Then update dp[i] to be max of dp[i] + 1 and dp[j].
"""


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
            stack.append(i)
        return max(dp)
