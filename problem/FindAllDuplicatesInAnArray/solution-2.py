class Solution:
    def cyclicSort(self, nums):
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[correct] != nums[i]:
                nums[correct], nums[i] = nums[i], nums[correct]
            else:
                i += 1

    def findDuplicates(self, nums: List[int]) -> List[int]:
        self.cyclicSort(nums)
        output = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                output.append(nums[i])
        return output
