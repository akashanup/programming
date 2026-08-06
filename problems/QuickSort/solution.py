class Solution:
    def partition(self, nums, start, end):
        pivot = nums[end]
        x = start - 1
        for i in range(start, end):
            if nums[i] <= pivot:
                x += 1
                nums[x], nums[i] = nums[i], nums[x]
        nums[x+1], nums[end] = nums[end], nums[x+1]
        return x+1

    def quickSort(self, nums, start, end):
        if start < end:
            pivotIndex = self.partition(nums, start, end)
            self.quickSort(nums, start, pivotIndex-1)
            self.quickSort(nums, pivotIndex+1, end)
        return nums


print(Solution().quickSort([12, 11, 13, 5, 6, 7], 0, 5))
