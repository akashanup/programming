"""
# Intuition

Since the array is already sorted in non-decreasing order, duplicate elements will always appear next to each other. We can maintain a pointer `k` that tracks the position where the next unique element should be placed.

As we traverse the array, whenever we encounter a number different from its previous element, we know it is a new unique value. We place it at index `k` and increment `k`.

# Approach

1. Handle the edge case where the array is empty.
2. Initialize `k = 1` since the first element is always unique.
3. Iterate through the array starting from index `1`.
4. For each element:
   - If it is different from the previous element, place it at `nums[k]`.
   - Increment `k`.
5. After the traversal, the first `k` positions of the array contain all unique elements in sorted order.
6. Return `k`.

# Complexity

- Time complexity:
  - **O(n)**, where `n` is the length of the array. We traverse the array exactly once.

- Space complexity:
  - **O(1)**, since the modification is done in-place without using extra space.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k