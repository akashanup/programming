class Solution:
    def findPivot(self, nums):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if mid < end and nums[mid] > nums[mid + 1]:
                return mid
            elif mid > start and nums[mid] < nums[mid - 1]:
                return mid - 1
            elif nums[mid] > nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return start

    def binarySearch(self, nums, start, end, target):
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivotIndex = self.findPivot(nums)
        targetIndex = self.binarySearch(nums, 0, pivotIndex, target)
        return targetIndex if targetIndex != -1 else self.binarySearch(nums, pivotIndex+1, len(nums)-1, target)
