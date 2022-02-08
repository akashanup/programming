class Solution:
    def dp(self, nums, index, lookup):
        if index == 0:
            return 1
        if lookup[index] == -1:
            lis = 1
            for i in range(index-1, -1, -1):
                if nums[i] < nums[index]:
                   lis = max(lis, 1 + self.dp(nums, i, lookup))
            lookup[index] = lis
        return lookup[index]

    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = 1
        lookup = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            lis = max(lis, self.dp(nums, i, lookup))
        return lis

