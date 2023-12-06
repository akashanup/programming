from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                return mid
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
        return -1


print(Solution().search([5, 6, 7, 1, 2, 3, 4], 2))
print(Solution().search([5, 6, 7, 1, 2, 3, 4], 21))
print(Solution().search([5, 6, 7, 1, 2, 2, 3, 3, 4, 5], 2))
print(Solution().search([5, 6, 7, 1, 2, 2, 3, 3, 4, 5], 5))
print(Solution().search([5, 6, 7, 1, 2, 2, 3, 3, 4], 1))
print(Solution().search([5, 6, 7, 1, 2, 2, 3, 3, 4], 3))
print(Solution().search([5, 6, 7, 1, 2, 2, 3, 3, 4, 5], 11))
