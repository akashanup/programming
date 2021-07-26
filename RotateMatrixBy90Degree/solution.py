class Solution:
    def printMatrix(self, matrix):
        n = len(matrix)
        for row in range(n):
            for col in range(n):
                print(matrix[row][col], end=" ")
            print()

    def transpose(self, matrix):
        n = len(matrix)
        for row in range(n):
            for col in range(row, n):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
        return matrix

    def reverseColumns(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[j][i], matrix[n - j - 1][i] = matrix[n - j - 1][i], matrix[j][i]
        return matrix

    def rotateBy90(self, matrix):
        # Transpose
        self.transpose(matrix)
        # print("Transpose:")
        # self.printMatrix(matrix)
        # Reverse columns
        self.reverseColumns(matrix)
        return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Solution().printMatrix(matrix)
rMatrix = Solution().rotateBy90(matrix)
print("Rotated by 90 degree anticlockwise:")
Solution().printMatrix(rMatrix)
