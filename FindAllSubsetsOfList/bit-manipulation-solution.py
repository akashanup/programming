class Solution:
    def getAllSubLists(self, nums):
        subsets = []
        n = len(nums)
        bits = 2 ** n
        for bit in range(bits):
            temp = []
            for num in range(n):
                if bit & (1 << num) > 0:
                    temp.append(nums[num])
            subsets.append(temp)
        return subsets


print(Solution().getAllSubLists([1, 2, 3]))
