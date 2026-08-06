class Solution:
    def dp(self, matrix, r, c, lookup):
        if r < len(matrix) and c < len(matrix[0]):
            if matrix[r][c] == "1":
                if lookup[r][c] == -1:
                    left = self.dp(matrix, r, c+1, lookup)
                    up = self.dp(matrix, r+1, c, lookup)
                    diagonal = self.dp(matrix, r+1, c+1, lookup)
                    lookup[r][c] = 1 + min(left, up, diagonal)
            else:
                lookup[r][c] = 0
            return lookup[r][c]
        return 0

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxSideLen = 0
        lookup = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "1":
                    maxSideLen = max(maxSideLen, self.dp(matrix, r, c, lookup))
        return maxSideLen*maxSideLen
