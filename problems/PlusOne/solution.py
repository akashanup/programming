"""
Intuition

We only need to add `1` to the number represented by the array. The addition starts from the least significant digit (the last element).

- If the current digit is less than `9`, we can increment it and return immediately.
- If the digit is `9`, it becomes `0` and generates a carry.
- The carry continues propagating through all trailing `9`s.
- If every digit is `9`, the result gains a new leading digit `1` (e.g., `999 -> 1000`).

# Approach

1. Start from the last digit.
2. Change all trailing `9`s to `0` while moving left.
3. If a digit smaller than `9` is found:
   - Increment it by `1`.
   - Return the modified array.
4. If no such digit exists, all digits were `9`.
   - Append a `0` at the end.
   - Set the first digit to `1`.
   - Return the resulting array.

# Complexity

- Time complexity:
  - $$O(n)$$
  
  In the worst case, every digit is `9` and we traverse the entire array once.

- Space complexity:
  - $$O(1)$$
  
  The modification is done in-place without using any extra data structures.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1

        # Propagate carry through trailing 9s
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        # Found a digit less than 9
        if i >= 0:
            digits[i] += 1
            return digits

        # All digits were 9 (e.g. 999 -> 1000)
        digits.append(0)
        digits[0] = 1

        return digits
