class Solution:

    """
        This algorithm will only work if the array is either increasing, or decreasing or increasing then decreasing.
        [NOTE] This algorithm will NOT work in case of decreasing then increasing sequence.
    """
    def binarySearch(self, nums):
        start = 0
        end = len(nums)
        while start < end:
            mid = start + ((end - start) // 2)
            if nums[mid - 1] <= nums[mid] <= nums[mid + 1]:
                # Increasing sequence at this index.
                start = mid + 1
            elif nums[mid - 1] >= nums[mid] >= nums[mid + 1]:
                # Decreasing sequence at this index.
                end = mid - 1
            elif nums[mid - 1] <= nums[mid] >= nums[mid + 1]:
                # Increasing and then decreasing at this index.
                # Max value is present at this index.
                return nums[mid]
