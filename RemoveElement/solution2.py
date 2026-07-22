"""
# Intuition
We need to remove all occurrences of `val` in-place and return the count of remaining elements. Since the elements after the valid portion of the array do not matter, we can use a pointer `k` to track the position where the next valid element should be placed.

# Approach
- Initialize a pointer `k = 0`.
- Traverse the array once.
- For every element that is not equal to `val`, place it at index `k` and increment `k`.
- By the end of the traversal, the first `k` elements of the array will contain all valid elements.
- Return `k` as the number of elements not equal to `val`.

# Complexity
- Time complexity:
  - `O(n)` where `n` is the length of the array, since we traverse it once.

- Space complexity:
  - `O(1)` since the modification is done in-place without using extra space.

"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k
