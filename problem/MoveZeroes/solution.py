"""
## Intuition

We want to move all non-zero elements to the front while preserving their relative order and doing everything in-place.

Instead of swapping elements, we maintain a pointer `k` that represents the next position where a non-zero element should be placed. As we iterate through the array, every non-zero element is moved to index `k`. If the element was moved from a different position (`i != k`), we immediately set its old position to `0`.

This allows us to compact all non-zero elements toward the beginning of the array while naturally pushing zeros toward the end in a single pass.

## Approach

- Initialize a pointer `k = 0`.
- Traverse the array using index `i`.
- If `nums[i]` is non-zero:
  - Place it at position `k`.
  - If `i != k`, set `nums[i]` to `0` because its value has been moved.
  - Increment `k`.
- After the traversal:
  - Indices `[0, k - 1]` contain all non-zero elements in their original order.
  - The remaining positions contain `0`s.

## Complexity

- Time complexity:
  - `O(n)`

- Space complexity:
  - `O(1)`

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]

                if i != k:
                    nums[i] = 0

                k += 1
