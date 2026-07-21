"""
# Intuition

We need to determine whether there exists a pair of numbers in the array such that one number is exactly double the other.

A brute-force approach would compare every pair of elements, resulting in **O(n²)** time complexity. Instead, we can use a hash set to keep track of previously seen numbers and efficiently check whether the current number's double or half has already appeared.

For every element `x`:

- If `2 * x` has already been seen, then a valid pair exists.
- If `x` is even and `x // 2` has already been seen, then a valid pair also exists.

This allows us to find the answer in a single pass through the array.

# Approach

1. Initialize an empty hash set `seen`.
2. Traverse the array from left to right.
3. For each number `x`:
   - Check if `2 * x` exists in `seen`.
   - If `x` is even, check if `x // 2` exists in `seen`.
   - If either condition is true, return `True`.
4. Add the current number to the hash set.
5. If no valid pair is found after traversing the array, return `False`.

# Complexity

- **Time complexity:** `O(n)`
  
  Each element is processed once, and hash set lookups take `O(1)` on average.

- **Space complexity:** `O(n)`
  
  In the worst case, all elements are stored in the hash set.

"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for x in arr:
            if 2 * x in seen:
                return True

            if x % 2 == 0 and x // 2 in seen:
                return True

            seen.add(x)

        return False