class Solution:
    def combinations(self, nums, combinationLength, targetSum, idx, combination):
        if targetSum == 0 and combinationLength == len(combination):
            return [combination]
        if targetSum < 0 or idx >= len(nums):
            return []
        return self.combinations(nums, combinationLength, targetSum - nums[idx], idx+1, combination + [nums[idx]]) + self.combinations(nums, combinationLength, targetSum, idx+1, combination)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [_ for _ in range(1, 10)]
        return self.combinations(nums, k, n, 0, [])
