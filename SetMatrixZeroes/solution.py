class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    for i in range(m):
                        if matrix[i][col] != 0:
                            matrix[i][col] = None
                    for j in range(n):
                        if matrix[row][j] != 0:
                            matrix[row][j] = None

        for row in range(m):
            for col in range(n):
                if matrix[row][col] is None:
                    matrix[row][col] = 0
