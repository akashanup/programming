"""
# Intuition
To determine whether the student qualifies for the attendance award, we need to track:

- The total number of absences ('A').
- The number of consecutive late days ('L').

While iterating through the attendance record:

- Count how many times 'A' appears.
- Keep track of consecutive 'L' characters.
- Reset the late counter whenever a non-'L' character appears.
- If the late counter reaches 3, the student immediately becomes ineligible.

# Approach
1. Initialize:
    - A to count absences.
    - L to count consecutive late days.
2. Traverse the string character by character:
    - If the character is 'A':
        - Increment absence count.
        - Reset consecutive late count.
    - If the character is 'L':
        - Increment consecutive late count.
    - Otherwise ('P'):
        - Reset consecutive late count.
3. If consecutive late count becomes 3, return False.
4. After traversal, return whether the absence count is less than 2.

# Complexity
- Time complexity: $$O(n)$$. We traverse the attendance record only once.

- Space complexity: $$O(1)$$. Only constant extra variables are used.
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        A = 0
        L = 0
        for ch in s:
            if ch == "A":
                A += 1
                L = 0
            elif ch == "L":
                L += 1
            else:
                L = 0
            if L == 3:
                return False
        return A < 2