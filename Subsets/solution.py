class Solution:
    def subsets(self, nums: List[int], subset=[]) -> List[List[int]]:
        return self.subsets(nums[1:], subset+[nums[0]]) + self.subsets(nums[1:], subset) if nums else [subset]
