from typing import List


class Solution:
    def binarySearchInRotatedArray(self, nums, start, end, target):
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                return True
            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False

    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1

        # We can't directly apply binarySearchInRotatedArray as long as the nums at start and end are same because
        # we won't be able to decide the part of the array we need to search.
        # So as long as nums at start and end are same and do not equal to target, skip these nums.
        while start <= end and nums[start] == nums[end]:
            if nums[start] == target:
                return True
            start += 1
            end -= 1

        # Now apply binarySearchInRotatedArray.
        return self.binarySearchInRotatedArray(nums, start, end, target)


print(Solution().search([5, 6, 7, 1, 2, 3, 4], 2))
print(Solution().search([5, 6, 7, 1, 2, 3, 4], 21))
print(Solution().search([5, 6, 7, 1, 2, 2, 3, 3, 4, 5], 2))
print(Solution().search([5, 6, 7, 1, 2, 2, 3, 3, 4, 5], 1))
print(Solution().search([5, 6, 7, 1, 2, 2, 3, 3, 4, 5], 11))
