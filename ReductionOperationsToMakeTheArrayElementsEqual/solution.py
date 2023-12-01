class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operations = 0
        # Start reducing the largest number to the second-largest number.
        for i in range(len(nums) - 2, -1, -1):
            # Find the second largest and largest with smallest i.
            if nums[i] != nums[i + 1]:
                # Number of operations required to reduce all the numbers at the right of i to nums[i]
                operations += len(nums) - (i + 1)

        return operations