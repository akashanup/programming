class Solution:
    def recur(self, nums, n, subLists, index, temp):
        subLists.append(temp.copy())
        for i in range(index, n):
            temp.append(nums[i])
            self.recur(nums, n, subLists, i+1, temp)
            temp.pop()
        return subLists

    def getAllSubLists(self, nums):
        return self.recur(nums, len(nums), [], 0, [])


print(Solution().getAllSubLists([1, 2, 3]))
