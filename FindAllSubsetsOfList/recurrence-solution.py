class Solution:
    def recur(self, nums, n, subLists, i, temp):
        if i < n:
            temp.append(nums[i])
            subLists.append(temp.copy())
            self.recur(nums, n, subLists, i+1, temp)
            temp.pop()
            self.recur(nums, n, subLists, i+1, temp)
        return subLists

    def getAllSubLists(self, nums):
        return self.recur(nums, len(nums), [[]], 0, [])


print(Solution().getAllSubLists([1, 2, 3]))
