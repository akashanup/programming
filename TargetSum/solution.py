class Solution:
    def recur(self, nums, i, n, target, waysSum, lookup):
        if n == i:
            return 1 if waysSum == target else 0
        else:
            if (i, waysSum) in lookup:
                return lookup[(i, waysSum)]
            lookup[(i, waysSum)] = self.recur(nums, i + 1, n, target, waysSum + nums[i], lookup) + self.recur(nums, i + 1, n, target, waysSum - nums[i], lookup)
            return lookup[(i, waysSum)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 1 if abs(nums[0]) == abs(target) else 0
        lookup = {}
        return self.recur(nums, 0, n, target, 0, lookup)
