class Solution:
    def cycleSort(self, nums):
        i = 0
        while i < len(nums):
            # Correct index of this encountered element is the value of element - 1 (i.e, nums[i] - 1) since the elements are in range 1-N and array is 0-indexed.
            correct = nums[i] - 1
            """
                In case of decreasing order, update the above statement with the below-
                correct = len(nums) - nums[i]
            """
            # Check whether this encountered element is equal to the element at its correct index.
            # If yes then move further, Else swap it with its correct index.
            if nums[i] == nums[correct]:
                i += 1
            else:
                # swap
                nums[i], nums[correct] = nums[correct], nums[i]
        return nums


print(Solution().cycleSort([2, 1, 5, 4, 3]))
print(Solution().cycleSort([1, 2, 3, 4, 5]))
print(Solution().cycleSort([5, 4, 3, 2, 1]))
