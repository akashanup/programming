class Solution:
    def getAllSubLists(self, nums):
        subLists = [[]]
        for i in range(len(nums) + 1):
            for j in range(i):
                subLists.append(nums[j:i])
        return subLists


print(Solution().getAllSubLists([1, 2, 3]))
