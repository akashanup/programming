"""
# Intuition
The spiral traversal can be viewed as simulating movement in four directions: **right → down → left → up**.

Instead of traversing one boundary at a time, we keep moving cell by cell in the current direction. Whenever we hit the current boundary, we:
1. Shrink that boundary since it has been fully processed.
2. Change the direction.
3. Continue from the next valid cell.

We maintain four boundaries:
- `ri` = top boundary
- `rf` = bottom boundary
- `ci` = left boundary
- `cf` = right boundary

Each completed side of the spiral causes one of these boundaries to move inward.

# Approach
1. Start from the top-left corner `(0, 0)` and move right.
2. Keep track of the current direction using:
   - `0 = right`
   - `1 = down`
   - `2 = left`
   - `3 = up`
3. For each of the `m * n` cells:
   - Add the current element to the answer.
   - Check whether the current boundary has been reached.
   - If yes, shrink the corresponding boundary and change direction.
   - Otherwise, continue moving in the same direction.
4. Since exactly one element is visited in each iteration and there are `m * n` iterations, every cell is visited exactly once.

# Complexity

- Time complexity:
  - $$O(m \times n)$$

- Space complexity:
  - $$O(1)$$ extra space (excluding the output array)

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        direction = 0  # 0=right, 1=down, 2=left, 3=up
        
        m, n = len(matrix), len(matrix[0])
        r, c = 0, 0
        ri, ci = 0, 0
        rf, cf = m-1, n-1

        for _ in range(m * n):
            ans.append(matrix[r][c])

            if direction == 0:  # right
                if c == cf:
                    ri += 1
                    direction = 1
                    r += 1
                else:
                    c += 1

            elif direction == 1:  # down
                if r == rf:
                    cf -= 1
                    direction = 2
                    c -= 1
                else:
                    r += 1

            elif direction == 2:  # left
                if c == ci:
                    rf -= 1
                    direction = 3
                    r -= 1
                else:
                    c -= 1

            else:  # up
                if r == ri:
                    ci += 1
                    direction = 0
                    c += 1
                else:
                    r -= 1

        return ans