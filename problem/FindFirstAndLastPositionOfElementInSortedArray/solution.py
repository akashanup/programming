class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        numberFound = False
        result = [-1, -1]
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                numberFound = True
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if not numberFound:
            return result
        result[1] = start - 1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                numberFound = True
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        result[0] = end + 1
        return result
