"""
# Intuition

The pivot index is the position where the sum of elements on the left is equal to the sum of elements on the right.

Instead of calculating left and right sums for every index separately (which would be inefficient), we first compute the total sum of the array. While traversing the array, we maintain a running `leftSum`.

For a pivot index `i`:

- Left sum = `leftSum`
- Right sum = `total - leftSum - nums[i]`

Rearranging the equation:

`leftSum == total - leftSum - nums[i]`

becomes:

`leftSum + nums[i] == total - leftSum`

This allows us to check the pivot condition in `O(1)` time for each index.

# Approach

1. Calculate the total sum of the array.
2. Initialize `leftSum = 0`.
3. Traverse the array:
   - Check if `leftSum + nums[i] == total - leftSum`.
   - If true, return the current index as the pivot index.
   - Otherwise, add the current element to `leftSum`.
4. If no pivot index is found after the traversal, return `-1`.

# Complexity

- Time complexity:
  - **O(n)**, where `n` is the length of the array. We traverse the array once.

- Space complexity:
  - **O(1)**, since only a few extra variables are used.
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0

        for i, num in enumerate(nums):
            if leftSum + num == total - leftSum:
                return i

            leftSum += num

        return -1