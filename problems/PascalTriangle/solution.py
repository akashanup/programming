"""
# Intuition
Pascal's Triangle follows a simple pattern: every row starts and ends with `1`, and each middle element is the sum of the two adjacent elements from the previous row.

Instead of computing values using combinations or recursion, we can build the triangle row by row using the previously generated row.

# Approach
1. Initialize the answer with the first row: `[[1]]`.
2. For each subsequent row:
   - Take the previous row.
   - Start the current row with `1`.
   - Generate the middle elements by summing adjacent elements from the previous row.
   - Append the ending `1`.
3. Add the completed row to the answer.
4. Return the generated triangle.

# Complexity
- Time complexity:
  - **O(numRows²)**

- Space complexity:
  - **O(numRows²)**

"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for _ in range(1, numRows):
            prev = ans[-1]
            curr = [1]

            for j in range(1, len(prev)):
                curr.append(prev[j - 1] + prev[j])

            curr.append(1)
            ans.append(curr)

        return ans