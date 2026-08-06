class Solution:
    def recur(self, nums, lookup, temp, key):
        lookup.add(tuple(sorted(temp.copy())))
        for i in range(key, len(nums)):
            temp.append(nums[i])
            self.recur(nums, lookup, temp, i + 1)
            temp.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lookup = set()
        self.recur(nums, lookup, [], 0)
        return [list(i) for i in lookup]
