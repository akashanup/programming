class Solution:
    def canMakeTriangle(self, nums, i):
        start = 0
        end = i - 1
        triangle = 0
        while start < end:
            if nums[start] + nums[end] > nums[i]:
                triangle += end - start
                end -= 1
            else:
                start += 1
        return triangle

    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        triangle = 0
        for i in range(2, len(nums)):
            triangle += self.canMakeTriangle(nums, i)
        return triangle
