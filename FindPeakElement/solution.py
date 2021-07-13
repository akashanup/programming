import sys


class Solution:
    def recur(self, nums, l, r):
        if l == r:
            return l
        else:
            mid = l + ((r - l) // 2)
            if nums[mid] > nums[mid + 1]:
                return self.recur(nums, l, mid)
            else:
                return self.recur(nums, mid + 1, r)

    def findPeakElement(self, nums):
        return self.recur(nums, 0, len(nums) - 1)


print(Solution().findPeakElement(nums=[1, 2, 3, 1]))
print(Solution().findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4]))
print(Solution().findPeakElement(nums=[1]))
print(Solution().findPeakElement(nums=[1, 2]))
print(Solution().findPeakElement(nums=[2, 1]))
