class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for j in range(n)] for i in range(n)]

        num = 1
        rowS, rowE, colS, colE = 0, n-1, 0, n-1

        # Walk in spriral form while inserting the number at each cell will give the result.
        while rowE >= 0 and colE >= 0:
            if rowS <= rowE:
                for col in range(colS, colE+1):
                    matrix[rowS][col] = num
                    num += 1
            rowS += 1

            if colS <= colE:
                for row in range(rowS, rowE+1):
                    matrix[row][colE] = num
                    num += 1
            colE -= 1

            if rowS <= rowE:
                for col in range(colE, colS-1, -1):
                    matrix[rowE][col] = num
                    num += 1
            rowE -= 1

            if colS <= colE:
                for row in range(rowE, rowS-1, -1):
                    matrix[row][colS] = num
                    num += 1
            colS += 1
        return matrix
