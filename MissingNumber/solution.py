class Solution:
    def cyclicSort(self, nums, n):
        i = 0
        while i < n:
            if nums[i] != n:
                correct = nums[i]
                if nums[i] != nums[correct]:
                    nums[i], nums[correct] = nums[correct], nums[i]
                else:
                    i += 1
            else:
                i += 1

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        self.cyclicSort(nums, n)
        """
            Since the numbers are in range 0 to n in 0-index array, therefore for each index i, the value present at i should also be i (Because we have soted the array).
            If it is not i then that number is missing.
        """
        for i in range(n):
            if i != nums[i]:
                return i
        return n


print(Solution().missingNumber([2, 3, 0, 4]))
print(Solution().missingNumber([2, 3, 0, 1]))
print(Solution().missingNumber([2, 4, 0, 1]))
print(Solution().missingNumber([3, 4, 0, 1]))
print(Solution().missingNumber([3, 4, 2, 1]))
