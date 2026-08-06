class Solution:
    def isArithmetic(self, nums, index):
        return nums[index] - nums[index-1] == nums[index-1] - nums[index-2]

    def dp(self, nums, index, lookup):
		# Base case: Minimum length of arithmetic subarray should be 3.
        if index < 2:
            lookup[index] = 0
		# If length is 3 then just check whether arithmetic property fulfills or not and return 1 if it fullfils.
        elif index == 2:
            lookup[index] = int(self.isArithmetic(nums, index))
        else:
			# Calculate the number of arithmetic subarrays till previous index so that they can be added if the current index fulfills the arithmetic property.
            previousCount = self.dp(nums, index-1, lookup)
			# If arithmetic subarrays can be extended from previous index to current index
            if self.isArithmetic(nums, index):
                lookup[index] = previousCount + 1
            else:
                lookup[index] = 0
        return lookup[index]

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        lookup = [0 for _ in range(len(nums))]
        self.dp(nums, len(nums)-1, lookup)
        return sum(lookup)
