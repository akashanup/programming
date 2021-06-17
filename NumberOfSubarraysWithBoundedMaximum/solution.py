class Solution:
    def generateCombinations(self, temp, left, right, lookup):
        for i in range(len(temp) + 1):
            for j in range(i):
                temp1 = temp[j:i]
                if len(temp1) and left <= max(temp1) <= right:
                    lookup.append(temp1)

    def numSubarrayBoundedMax(self, nums, left, right):
        lookup = []
        i = 0
        maxVal = -1
        for key, val in enumerate(nums):
            maxVal = max(maxVal, val)
            if left <= maxVal <= right and val <= maxVal:
                if key == len(nums) - 1:
                    self.generateCombinations(nums[i:key + 1], left, right, lookup)
            else:
                if maxVal >= right:
                    self.generateCombinations(nums[i:key], left, right, lookup)
                    i = key + 1
                maxVal = -1
        return len(lookup)


# print(Solution().numSubarrayBoundedMax([2, 1], 2, 3))
# print(Solution().numSubarrayBoundedMax([2, 1, 4, 3, 4, 1, 2], 2, 3))
# print(Solution().numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))
# import random
# nums = [random.randint(1, 10) for i in range(10)]
# left = random.randint(1, 5)
# right = random.randint(5, 10)
nums = [5, 4, 3, 7, 5, 7, 6, 8, 9, 8]
nums = [5, 4, 3, 7, 5, 7, 10, 6, 8, 9, 8]
left = 4
right = 9
print(nums)
print(left)
print(right)
print(Solution().numSubarrayBoundedMax(nums, left, right))
