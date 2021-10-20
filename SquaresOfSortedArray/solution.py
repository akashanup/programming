class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        firstNonNegativeNumberIndex = None
        for index, value in enumerate(nums):
            if value > -1:
                firstNonNegativeNumberIndex = index
                break

        n = len(nums)
        for i in range(n):
            nums[i] **= 2

        # All negative numbers
        if firstNonNegativeNumberIndex is None:
            return nums[::-1]

        # No non negative number
        if firstNonNegativeNumberIndex == 0:
            return nums

        """
            Now consider that the array is sliced in two parts, one for all negative and the other for all neegative numbers.
            Since both the arrays are sorted, we can use the technique of merging two sorted arrays.
            Note that the array with negative numbers must be reversed to make it sorted in non-decreasing order.
        """
        nums[:firstNonNegativeNumberIndex] = nums[:firstNonNegativeNumberIndex][::-1]

        output = [None] * n
        i = 0
        j = firstNonNegativeNumberIndex
        k = 0

        while i < firstNonNegativeNumberIndex and j < n:
            if nums[i] < nums[j]:
                output[k] = nums[i]
                k += 1
                i += 1
            else:
                output[k] = nums[j]
                k += 1
                j += 1

        while i < firstNonNegativeNumberIndex:
            output[k] = nums[i]
            k += 1
            i += 1

        while j < n:
            output[k] = nums[j]
            k += 1
            j += 1

        return output

