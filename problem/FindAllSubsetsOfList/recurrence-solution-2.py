"""
If nums has duplicates.
"""


class Solution:
    def recur(self, nums, n, subLists, i, temp):
        if i < n:
            if i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            temp.append(nums[i])
            subLists.append(temp.copy())
            self.recur(nums, n, subLists, i + 1, temp)
            temp.pop()
            self.recur(nums, n, subLists, i + 1, temp)
        return subLists

    def getAllSubLists(self, nums):
        nums.sort()
        return self.recur(nums, len(nums), [[]], 0, [])


print(Solution().getAllSubLists([1, 2, 3, 3, 2]))
