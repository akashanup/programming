"""
# Intuition

Since the order of elements does not matter, instead of shifting all elements left whenever `val` is found, we can replace the unwanted element with an element from the end of the array.

We maintain two pointers:

- `i` scans the array from the beginning.
- `j` points to the last valid element from the end.

If `nums[i]` equals `val`, we find the next non-`val` element from the right and place it at index `i`. Then we shrink the valid range by moving `j` left. This effectively removes occurrences of `val` without extra space.

# Approach

1. Initialize two pointers:
   - `i = 0` (start of array)
   - `j = len(nums) - 1` (end of array)

2. Traverse while `i <= j`:
   - If `nums[i] == val`:
     - Skip all trailing occurrences of `val` from the right.
     - Replace `nums[i]` with `nums[j]`.
     - Decrement `j` to shrink the valid portion of the array.
   - Move `i` forward.

3. After the[j - Decrement `j` to shrink the e contained within indices `[0, j]`.

4. Return `j + 1`, which represents the count of elements not equal to `val`.

# Complexity

- Time complexity:
  - **O(n)**
  
  Each element is processed at most once by either pointer.

- Space complexity:
  - **O(1)**

  The operation is performed in-place without using extra space.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            if nums[i] == val:
                while i < j and nums[j] == val:
                    j -= 1

                nums[i] = nums[j]
                j -= 1

            i += 1

        return j + 1