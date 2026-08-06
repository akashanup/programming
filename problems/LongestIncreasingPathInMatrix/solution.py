class Solution:
    DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    def dp(self, matrix, r, c, lookup):
        if lookup[r][c] == -1:
            path = 0
            for dr, dc in Solution.DIRECTIONS:
                row, col = r+dr, c+dc
                if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] > matrix[r][c]:
                    path = max(path, 1+self.dp(matrix, row, col, lookup))
            lookup[r][c] = path
        return lookup[r][c]
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        lookup = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        lip = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                lip = max(lip, 1+self.dp(matrix, r, c, lookup))
        
        return lip
