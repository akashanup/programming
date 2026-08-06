class Solution:
    def recur(self, nums, n, k, index, temp, subLists):
        if k == 0:
            subLists.append(temp.copy())
        else:
            for i in range(index, n):
                temp.append(nums[i])
                self.recur(nums, n, k-1, i+1, temp, subLists)
                temp.pop()
        return subLists

    def getAllSubLists(self, nums, k):
        return self.recur(nums, len(nums), k, 0, [], [])


print(Solution().getAllSubLists([1, 2, 3, 4, 5], 3))
