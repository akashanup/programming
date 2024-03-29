class Solution:
    def cyclicSort(self, nums, n):
        i = 0
        while i < n:
            correct = nums[i]
            # Since nums[i] starts from zero and can be equal to n, hence we need to check for upper bound also.
            if nums[i] < len(nums) and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        self.cyclicSort(nums, n)
        """
            Since the numbers are in range 0 to n in 0-index array, therefore for each index i, the value present at i 
            should also be i (Because we have sorted the array).
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
