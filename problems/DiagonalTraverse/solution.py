"""
# Intuition

All elements belonging to the same diagonal have the same value of:

$$
r + c
$$

where `r` is the row index and `c` is the column index.

For example:

```text
[
      0   1   2   3
  0 [ 1,  2,  3,  4 ]
  1 [ 5,  6,  7,  8 ]
  2 [ 9, 10, 11, 12 ]
]
```

Diagonals can be grouped as:

```text
 First Diagonal: ((0,0)) => Sum = 0
Second Diagonal: ((0,1), (1,0)) => Sum = 1
Third Diagonal: ((0,2), (1,1), (2,0)) => Sum = 2
Fourth Diagonal: ((0,3), (1,2), (2,1)) => Sum = 3
Fifth Diagonal: ((1,3), (2,2)) => Sum = 4
Sixth Diagonal: ((2,3)) => Sum = 5
```

Since the maximum value of `r + c` is:

$$
(m - 1) + (n - 1) = m + n - 2
$$

we can store all elements having the same index sum into the same bucket (diagonal).

The required traversal alternates directions across diagonals:

- Even-indexed diagonals are traversed in reverse order.
- Odd-indexed diagonals are traversed in normal order.

---

# Approach

1. Create `m + n - 1` buckets to store the diagonals.
2. Traverse the matrix once and append each element into the bucket corresponding to its diagonal index `r + c`.
3. Iterate through all diagonals:
   - If the diagonal index is even, append its elements in reverse order.
   - Otherwise append them in their original order.
4. Return the accumulated result.

---

# Complexity

- Time complexity:

$$
O(m * n)
$$

We visit every cell exactly once while building the diagonals and every element exactly once while constructing the answer.

- Space complexity:

$$
O(m * n)
$$

The auxiliary diagonal buckets store all matrix elements.

---
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        diagonals = [[] for _ in range(m + n - 1)]

        for r in range(m):
            for c in range(n):
                diagonals[r + c].append(mat[r][c])

        output = []
        i = 0

        while i <= m + n - 2:
            output += diagonals[i] if i % 2 else diagonals[i][::-1]
            i += 1

        return output