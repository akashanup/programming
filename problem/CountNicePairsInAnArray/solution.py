"""
Logic:
    Given formula => nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
    Let us try to rearrange the given formula to, nums[i] - rev(nums[i]) == nums[j] + rev(nums[j]).
    After rearranging the formula, the problem is simplified as now we are only interested in nums[i] - rev(nums[i]).
    So in the given array if we find some pair (i, j) where nums[i] - rev(nums[i]) == nums[j] + rev(nums[j]) then
    we have our one nice pair.
    Let us try to create a hashmap which stores the key as nums[i] - rev(nums[i]) and its count as value for each i.
    Now for all the values of hashmap which are greater than 1, we can say that we have found some nice pairs.
    Let's say for some value x its count is n(>1) in hashmap, the total number of nice pairs for x would be nC2
    i.e., (n * (n-1)) / 2
"""


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        lookup = {}
        for num in nums:
            revNum = int(str(num)[::-1])
            diff = num - revNum
            if diff not in lookup:
                lookup[diff] = 0
            lookup[diff] += 1
        nicePairsCount = 0
        for value in lookup.values():
            if value > 1:
                nicePairsCount += (value * (value - 1)) // 2
        return nicePairsCount % ((10 ** 9) + 7)
