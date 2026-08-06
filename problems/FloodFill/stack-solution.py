class Solution:
    def dfs(self, grid, row, col, fillColor, currentColor):
        for r, c in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == currentColor:
                grid[r][c] = fillColor
                self.dfs(grid, r, c, fillColor, currentColor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        self.dfs(image, sr, sc, color, image[sr][sc])
        image[sr][sc] = color
        return image
