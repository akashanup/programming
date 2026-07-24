"""
# Intuition

Since every number in the array lies in the range `[1, n]`, each number has a unique correct position in the array:

- `1` should be at index `0`
- `2` should be at index `1`
- ...
- `n` should be at index `n - 1`

We can repeatedly place each number at its correct position using Cyclic Sort. After the array is rearranged, any index that does not contain its expected value indicates that the corresponding number is missing.

# Approach

1. Iterate through the array using Cyclic Sort.
2. For each index `i`, compute the correct position of the current value:
   `correct = nums[i] - 1`.
3. If the current number is already in its correct position or a duplicate occupies that position, move to the next index.
4. Otherwise, swap the current element with the element at its correct position.
5. After sorting, scan the array once more.
6. If `nums[i] != i + 1`, then `i + 1` is missing from the array, so add it to the answer.

# Complexity

- Time complexity:

$$O(n)$$

Each swap places at least one element in its correct position, so the total number of swaps is bounded by `n`.

- Space complexity:

$$O(1)$$

Only a few variables are used, and the sorting is performed in-place.

"""

class Solution:
    def cycleSort(self, nums):
        i = 0

        while i < len(nums):
            correct = nums[i] - 1

            if nums[correct] == nums[i]:
                i += 1
            else:
                nums[correct], nums[i] = nums[i], nums[correct]

    def findDisappearedNumbers(self, nums: List[int]) -> Listself.cycleSort(nums)

        output = []

        for i in range(len(nums)):
            if nums[i] != i + 1:
                output.append(i + 1)

        return output