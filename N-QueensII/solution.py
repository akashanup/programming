class Solution:
    def isValidPosition(self, i, j, matrix):
        for row in range(i):
            if matrix[row] == j or abs(row - i) == abs(matrix[row] - j):
                return False
        return True

    def assignQueens(self, n, rowNum, currValues, matrix, res):
        if rowNum == n:
            res.append(currValues)
            return
        for j in range(n):
            if self.isValidPosition(rowNum, j, matrix):
                matrix[rowNum] = j
                self.assignQueens(n, rowNum + 1, currValues + ["." * j + "Q" + "." * (n - j - 1)], matrix, res)

    def solveNQueens(self, n):
        matrix = [-1] * n
        res = []
        self.assignQueens(n, 0, [], matrix, res)
        return len(res)


print(Solution().solveNQueens(1))
