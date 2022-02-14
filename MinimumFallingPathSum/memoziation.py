class Solution:
    def dp(self, matrix, r, c, lookup):
        if r == len(matrix):
            return 0
        if r > len(matrix) or c >= len(matrix[0]) or c < 0:
            return sys.maxsize
        if lookup[r][c] == -1:
            lookup[r][c] =  matrix[r][c] + min(self.dp(matrix, r+1, c-1, lookup), self.dp(matrix, r+1, c, lookup), self.dp(matrix, r+1, c+1, lookup))
        return lookup[r][c]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        minSum = sys.maxsize
        lookup = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for c in range(len(matrix[0])):
            minSum = min(minSum, self.dp(matrix, 0, c, lookup))
        return minSum
