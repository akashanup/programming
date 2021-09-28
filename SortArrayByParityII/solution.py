class Solution(object):
    def sortArrayByParityII(self, nums):
        odd = 1
        even = 0
        n = len(nums)

        while odd < n and even < n:
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 != 0:
                odd += 2
            else:
                nums[odd], nums[even] = nums[even], nums[odd]
        return nums
