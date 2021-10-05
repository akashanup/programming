class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        """
            Since the grid is sorted in non increasing order among rows and columns.
            So let's start searching from last row and first column for the negative value because numbers after that column and below that row will definitely be -ve.        
        """

        i, j = m-1, 0
        negatives = 0

        while i >= 0 and j < n:
            if grid[i][j] < 0:
                negatives += (n - j)
                i -= 1
            else:
                j += 1
        return negatives
