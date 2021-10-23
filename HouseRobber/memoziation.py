class Solution:
    def recur(self, nums, i, dp):
        if i == 0:
            return nums[0]
        if dp[i] is None:
            if i == 1:
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(nums[i]+self.recur(nums, i-2, dp), self.recur(nums, i-1, dp))
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return self.recur(nums, n-1, [None]*n)
