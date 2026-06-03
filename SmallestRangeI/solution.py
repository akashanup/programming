"""
# Intuition
To minimize the score (maximum element - minimum element), we should try to reduce the largest value and increase the smallest value.
Since each element can be changed by at most k:
- the maximum element can decrease by k
- the minimum element can increase by k

So the new possible score becomes:

- `(max(nums) - k) - (min(nums) + k)`

If this value becomes negative, the minimum possible score is 0.

# Approach
1. Find the maximum and minimum values in the array.
2. Reduce the maximum value by k.
3. Increase the minimum value by k.
4. Compute the new score.
5. Return the maximum between the computed score and 0.
This works because only the extreme values affect the score.

# Complexity
Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        score = max(nums) - k - (min(nums) + k)

        return max(score, 0)