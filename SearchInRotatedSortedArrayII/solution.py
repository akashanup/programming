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

            if nums[start] == nums[mid] == nums[end] and start < end:
                if nums[start] > nums[start + 1]:
                    return start
                start += 1
                if nums[end] < nums[end - 1]:
                    return end - 1
            elif nums[start] < nums[mid] or (nums[start] == nums[mid] and nums[mid] > nums[end]):
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

    def search(self, nums: List[int], target: int) -> bool:
        pivotIndex = self.findPivot(nums)
        targetIndex = self.binarySearch(nums, 0, pivotIndex, target)
        return True if targetIndex != -1 else (True if self.binarySearch(nums, pivotIndex + 1, len(nums) - 1, target) != -1 else False)
