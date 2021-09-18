class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        spiral = []
        row = 0
        col = 0
        while m >= 0 and n >= 0:
            if row <= m:
                for j in range(col, n+1):
                    spiral.append(matrix[row][j])
            row += 1
            if col <= n:
                for i in range(row, m+1):
                    spiral.append(matrix[i][n])
            n -= 1
            if row <= m:
                for j in range(n, col-1, -1):
                    spiral.append(matrix[m][j])
            m -= 1
            if col <= n:
                for i in range(m, row-1, -1):
                    spiral.append(matrix[i][col])
            col += 1
        return spiral
