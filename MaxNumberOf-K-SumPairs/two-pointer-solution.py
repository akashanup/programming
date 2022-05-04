class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        nums.sort()
        start, end = 0, len(nums)-1
        while start < end:
            currSum = nums[start] + nums[end]
            if currSum == k:
                operations += 1
                start += 1
                end -= 1
            elif currSum > k:
                end -= 1
            else:
                start += 1

        return operations
