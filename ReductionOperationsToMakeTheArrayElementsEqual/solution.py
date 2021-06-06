class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        if nums[0] == nums[-1]:
            return 0
        temp = {}
        j = 0
        n = 0
        while j < len(nums) - 1:
            n += 1
            if nums[j] != nums[j+1]:
                temp[nums[j]] = n
                n = 0
            j += 1
            temp[nums[j]] = n + 1
        temp.pop(nums[-1])
        count = 0
        reductions = 0
        for i in temp.values():
            count += i
            reductions += count
        return reductions
