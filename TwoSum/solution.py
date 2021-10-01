class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            counterPart = target - nums[i]
            if counterPart in hash:
                return [i, hash[counterPart]]
            hash[nums[i]] = i
