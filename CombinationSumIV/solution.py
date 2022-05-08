class Solution:
    def combinations(self, nums, target, combination, lookup):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target not in lookup:
            ans = 0
            for num in nums:
                ans += self.combinations(nums, target-num, combination+[num], lookup)
            lookup[target] = ans
        return lookup[target]

    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.combinations(nums, target, [], {})
