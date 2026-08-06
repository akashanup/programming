class Solution:
    def countingSort(self, nums, digit):
        lookup = [0] * 10
        for i in nums:
            index = i // (10 ** digit)
            lookup[index % 10] += 1
        i = 1
        while i < 10:
            lookup[i] += lookup[i - 1]
            i += 1
        sortedNums = [None] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            index = nums[i] // (10 ** digit)
            sortedNums[lookup[index % 10] - 1] = nums[i]
            lookup[index % 10] -= 1
        return sortedNums

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        for i in range(len(str(max(nums)))):
            nums = self.countingSort(nums, i)
        nums = [i for i in nums if i < 0] + [i for i in nums if i >= 0]
        longestSeq = 0
        sequence = 1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                sequence += 1
            else:
                if nums[i] != nums[i + 1]:
                    longestSeq = max(longestSeq, sequence)
                    sequence = 1
        longestSeq = max(longestSeq, sequence)
        return longestSeq
