"""
# Intuition

For every element, we need the greatest element on its right side.

A brute force solution would scan all elements to the right for each index, resulting in O(n²) time complexity. Instead, we can traverse the array from right to left while maintaining the maximum element seen so far (`right_max`).

At any index, `right_max` is exactly the answer that should replace the current element.

# Approach

1. Initialize `right_max = -1` because the last element has no elements to its right.
2. Traverse the array from right to left.
3. For each element:
   - Replace it with `right_max`.
   - Update `right_max` using the original value if it is larger.
4. Return the modified array.

This allows us to solve the problem in a single pass.

# Complexity

- Time complexity:
  - **O(n)**

- Space complexity:
  - **O(1)**

"""

class Solution:
    def replaceElements(self, arr):
        right_max = -1

        for i in range(len(arr) - 1, -1, -1):
            arr[i], right_max = right_max, max(right_max, arr[i])

        return arr