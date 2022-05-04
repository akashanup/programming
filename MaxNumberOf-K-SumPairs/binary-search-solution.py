class Solution:
    def binarySearch(self, nums, target, start, end):
        while start <= end:
            mid = start + ((end-start)//2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid -1
        return None

    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        nums.sort()
        i = 0
        while i < len(nums):
            num = nums[i]
            j = self.binarySearch(nums, k-num, i+1, len(nums)-1)
            if j is not None:
                nums.pop(j)
                nums.pop(i)
                operations += 1
            else:
                i += 1

        return operations
