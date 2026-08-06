"""
# Intuition

Since every number is guaranteed to be in the range `[1, n]`, we can use the input array itself to keep track of which numbers have been seen.

For a number `x`, we use index `x - 1` as its corresponding position in the array. Instead of using extra space, we mark a number as visited by adding `n` to its mapped index.

After processing all elements:

- If `nums[i] > n`, then the number `i + 1` appeared in the array.
- If `nums[i] <= n`, then the number `i + 1` never appeared and is missing.

# Approach

1. Iterate through the array.
2. For each element, recover its original value if it was previously marked by subtracting `n`.
3. Use the value as an index (`currentNum - 1`).
4. If the target position has not been marked yet (`<= n`), add `n` to mark it as visited.
5. Iterate through the array again.
6. Any position whose value is still `<= n` corresponds to a missing number, so add `i + 1` to the answer.

# Complexity

- Time complexity:

$$O(n)$$

- Space complexity:

$$O(1)$$

(Excluding the output array.)
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            currentNum = nums[i]

            if currentNum > n:
                currentNum -= n

            if nums[currentNum - 1] <= n:
                nums[currentNum - 1] += n

        answer = []

        for i in range(n):
            if nums[i] <= n:
                answer.append(i + 1)

        return answer