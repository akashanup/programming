"""
# Intuition

We need to traverse the matrix diagonally in a zig-zag fashion:

- Move **up-right (↗)** on one diagonal.
- Move **down-left (↙)** on the next diagonal.
- Whenever we hit a boundary, we change direction and move to the starting cell of the next diagonal.

Instead of storing all diagonals separately, we can directly simulate the traversal using the current cell `(r, c)` and a direction variable.

The tricky part is handling the boundary conditions correctly, especially at the corners where two boundaries can be hit simultaneously.

---

# Approach

1. Start from the top-left cell `(0, 0)`.
2. Maintain a variable `direction`:
   - `1` → moving up-right (`↗`)
   - `-1` → moving down-left (`↙`)
3. For each of the `m * n` elements:
   - Add the current element to the answer.
   - Move according to the current direction.
4. While moving up-right:
   - If we reach the right boundary, move down and reverse direction.
   - Else if we reach the top boundary, move right and reverse direction.
   - Otherwise continue moving up-right.
5. While moving down-left:
   - If we reach the bottom boundary, move right and reverse direction.
   - Else if we reach the left boundary, move down and reverse direction.
   - Otherwise continue moving down-left.
6. Continue until all elements are visited.

---

# Complexity

- Time complexity:

$$O(m \times n)$$

Each element is visited exactly once.

- Space complexity:

$$O(1)$$

Ignoring the output array, only a few variables are used.
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> Listm, n = len(mat), len(mat[0])

        r, c = 0, 0
        diagonalOrder = []

        # direction = 1 means up-right, -1 means down-left
        direction = 1

        for _ in range(m * n):
            diagonalOrder.append(mat[r][c])

            if direction == 1:
                if c == n - 1:
                    r += 1
                    direction = -1
                elif r == 0:
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                    direction = 1
                elif c == 0:
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1

        return diagonalOrder