"""
# Intuition
The main challenge is that duplicating a `0` shifts all subsequent elements to the right, which can overwrite values that haven't been processed yet.

Instead of shifting elements one by one, we can imagine an expanded version of the array where every `0` is duplicated. Then, using two pointers from the end, we copy elements backward into their correct positions. This prevents overwriting unprocessed elements and allows us to modify the array in-place.

# Approach
1. Count the number of zeros in the array.
2. Consider a virtual expanded array of size `n + zerosCount`.
3. Use:
   - `i` to point to the last element of the original array.
   - `j` to point to the last position of the virtual expanded array.
4. Traverse from right to left:
   - Copy `arr[i]` to position `j` if `j` lies within the bounds of the original array.
   - If `arr[i]` is `0`, duplicate it by writing another `0` at the previous position.
5. Continue until all elements have been processed.

By filling from the back, we avoid overwriting values that are still needed.

# Complexity
- Time complexity:
  - **O(n)**

- Space complexity:
  - **O(1)**
"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)

        # Count total zeros
        zerosCount = 0
        i = 0
        while i < n:
            if arr[i] == 0:
                zerosCount += 1
            i += 1

        # Two pointers:
        # i -> original array index
        # j -> virtual expanded array index
        i = n - 1
        j = n - 1 + zerosCount

        while i >= 0:
            if j < n:
                arr[j] = arr[i]

            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0

            i -= 1
            j -= 1