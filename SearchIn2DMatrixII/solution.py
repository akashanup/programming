class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Let us start searching (binary search) from 0th row and last column
        row = 0
        col = len(matrix[0]) - 1
        """
            If target is less then matrix[row][col] at any point then, since the elements are sorted from left to right in a row, we can guarntee that element will only be present before the current column.
            If target is greater then matrix[row][col] at any point then, since the elements are sorted from top to bottom in a column, we can guarntee that element will only be present after the current row.
            
        """
        while row <= len(matrix) - 1 and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

