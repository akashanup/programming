"""
# Intuition

We only need the top 3 **distinct** maximum values, not a fully sorted array.

While traversing the array once, maintain three variables:

- `m1` → largest distinct number seen so far
- `m2` → second largest distinct number
- `m3` → third largest distinct number

Whenever a larger number is found, shift the existing values down accordingly. Using strict inequalities naturally ignores duplicates because a number equal to any existing maximum will fail all update conditions.

# Approach

1. Initialize `m1`, `m2`, and `m3` to negative infinity.
2. Traverse the array:
   - If `num > m1`, shift `m1` to `m2`, `m2` to `m3`, and update `m1`.
   - Else if `m1 > num > m2`, update the second maximum and shift the previous second maximum to third.
   - Else if `m2 > num > m3`, update the third maximum.
3. After processing all elements:
   - If `m3` was updated, return it.
   - Otherwise, return `m1` since a third distinct maximum does not exist.

# Complexity

- Time complexity:
  - `O(n)`

- Space complexity:
  - `O(1)`

"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1 = m2 = m3 = float("-inf")

        for num in nums:
            if num > m1:
                m3 = m2
                m2 = m1
                m1 = num
            elif m1 > num > m2:
                m3 = m2
                m2 = num
            elif m2 > num > m3:
                m3 = num

        if m3 > float("-inf"):
            return m3

        return m1