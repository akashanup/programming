class Solution:
    def checkFor1s(self, matrix, i, j, layer):
        for x in range(layer + 1):
            if matrix[i + x][j + layer] == "0":
                return False
        for y in range(layer + 1):
            if matrix[i + layer][j + y] == "0":
                return False
        return True

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n, maxSideLen = len(matrix), len(matrix[0]), 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    maxSideLen = max(1, maxSideLen)
                    # Check whether it forms a square of 1s with side length of at least largestSquareLength and can become a larger square of all 1s.
                    if i + maxSideLen < m and j + maxSideLen < n:
                        # Check for all 1s in each subsequent layer and whether the side length can be increased.
                        layer = 1
                        while i + layer < m and j + layer < n and self.checkFor1s(matrix, i, j, layer):
                            layer += 1
                        maxSideLen = max(layer, maxSideLen)
        return maxSideLen * maxSideLen
