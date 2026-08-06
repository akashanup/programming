class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.calculatePrefixSum(matrix)

    def calculatePrefixSum(self, matrix):
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r > 0 and c > 0:
                    self.prefixSum[r][c] = self.prefixSum[r-1][c] + self.prefixSum[r][c-1] - self.prefixSum[r-1][c-1] + matrix[r][c]
                elif r > 0:
                    self.prefixSum[r][c] = self.prefixSum[r-1][c] + matrix[r][c]
                elif c > 0:
                    self.prefixSum[r][c] = self.prefixSum[r][c-1] + matrix[r][c]
                else:
                    self.prefixSum[r][c] = matrix[r][c]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0 and col1 > 0:
            return self.prefixSum[row2][col2] - self.prefixSum[row1-1][col2] - self.prefixSum[row2][col1-1] + self.prefixSum[row1-1][col1-1]
        elif row1 > 0:
            return self.prefixSum[row2][col2] - self.prefixSum[row1-1][col2]
        elif col1 > 0:
            return self.prefixSum[row2][col2] - self.prefixSum[row2][col1-1]
        else:
            return self.prefixSum[row2][col2]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
