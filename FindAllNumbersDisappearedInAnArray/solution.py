class Solution:
    def cycleSort(self, nums):
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[correct] == nums[i]:
                i += 1
            else:
                nums[correct], nums[i] = nums[i], nums[correct]

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        self.cycleSort(nums)
        output = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                output.append(i+1)
            i += 1
        return output

