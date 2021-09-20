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
        # This QuickSort requires O(Log n) auxiliary space in worst case.
        while start < end:
            pivotIndex = self.partition(nums, start, end)
            if pivotIndex - start < end - pivotIndex:
                self.quickSort(nums, start, pivotIndex-1)
                start = pivotIndex + 1
            else:
                self.quickSort(nums, pivotIndex+1, end)
                end = pivotIndex - 1
        return nums


print(Solution().quickSort([12, 11, 13, 5, 6, 7], 0, 5))
