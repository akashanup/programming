"""
## Intuition

We can think of the problem as compressing all non-zero elements to the beginning of the array while preserving their relative order.

Instead of swapping elements, we first place every non-zero element into the next available position. Once all non-zero elements have been moved to the front, the remaining positions are simply filled with `0`s.

This approach minimizes unnecessary operations and keeps the implementation simple and easy to reason about.

## Approach

- Maintain a pointer `k` indicating the next position where a non-zero element should be placed.
- Traverse the array:
  - If the current element is non-zero, write it to `nums[k]` and increment `k`.
- After all non-zero elements have been compacted to the front, fill the remaining positions from `k` to the end of the array with `0`s.

## Complexity

- Time complexity:
  - `O(n)`

- Space complexity:
  - `O(1)`

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0

        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1

        while k < len(nums):
            nums[k] = 0
            k += 1
