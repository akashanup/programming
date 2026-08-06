"""
# Intuition

Since the largest element in the array is guaranteed to be unique, we only need to keep track of the largest and second largest elements.

If the largest number is at least twice the second largest number, then it is automatically at least twice every other number in the array.

# Approach

1. Traverse the array once.
2. Maintain:
   - `largestNum` : the largest value seen so far.
   - `largestNumIdx` : the index of the largest value.
   - `secondLargestNum` : the second largest value seen so far.
3. Whenever a new largest element is found:
   - Update `secondLargestNum` with the previous largest value.
   - Update `largestNum` and its index.
4. Otherwise, update `secondLargestNum` if the current element is greater than it.
5. After the traversal:
   - If `largestNum >= 2 * secondLargestNum`, return the index of the largest element.
   - Otherwise, return `-1`.

# Complexity

- Time complexity:
  - $$O(n)$$

  We traverse the array only once.

- Space complexity:
  - $$O(1)$$

  Only a few extra variables are used regardless of the input size.

"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largestNum = -1
        largestNumIdx = -1
        secondLargestNum = -1

        for i in range(len(nums)):
            if nums[i] >= largestNum:
                secondLargestNum = largestNum
                largestNum = nums[i]
                largestNumIdx = i
            elif nums[i] > secondLargestNum:
                secondLargestNum = nums[i]

        if (2 * secondLargestNum) <= largestNum:
            return largestNumIdx

        return -1