class Solution:
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])
        output = []
        # Iterate over first diagonal
        for k in range(m):
            i = k
            j = 0
            while i >= 0:
                output.append(mat[i][j])
                i -= 1
                j += 1

        # Iterate over second diagonal
        for k in range(1, n):
            i = m - 1
            j = k
            while j < n:
                output.append(mat[i][j])
                i -= 1
                j += 1

        return output


print(Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]))
