class Solution:
    def isValid(self, matrix, n, row, col):
        for r in range(row):
            for c in range(n):
                if matrix[r][c] == 1:
                    if r == row or c == col:
                        return False
                    xf, yf = r, c
                    while xf < n and yf < n:
                        if xf == row and yf == col:
                            return False
                        xf += 1
                        yf += 1

                    xb, yb = r, c
                    while xb >= 0 and yb >= 0:
                        if xb == row and yb == col:
                            return False
                        xb -= 1
                        yb -= 1

                    xf, yb = r, c
                    while xf < n and yb >= 0:
                        if xf == row and yb == col:
                            return False
                        xf += 1
                        yb -= 1
                    xb, yf = r, c
                    while xb >= 0 and yf < n:
                        if xb == row and yf == col:
                            return False
                        xb -= 1
                        yf += 1
        return True

    def assignQueen(self, matrix, n, row, result):
        if row == n:
            result.append([m[:] for m in matrix])
            return

        for col in range(n):
            if matrix[row][col] == 0:
                if self.isValid(matrix, n, row, col):
                    matrix[row][col] = 1
                    self.assignQueen(matrix, n, row+1, result)
                    matrix[row][col] = 0

    def solveNQueens(self, n):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        result = []
        self.assignQueen(matrix, n, 0, result)
        return len(result)


print(Solution().solveNQueens(4))
