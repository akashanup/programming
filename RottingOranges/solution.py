class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
            This question is very similar to https://leetcode.com/problems/01-matrix.
            Here we just need to keep a track of all rotten oranges and assign 0 minutes to it.
            Now use BFS to check all its neighbours and add 1 to minutes which will indicate the time for a fresh orange to get rotten.
        """

        m = len(grid)
        n = len(grid[0])

        visited = [[None for _ in range(n)] for _ in range(m)]
        queue = []

        freshOranges = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    freshOranges += 1
                elif grid[row][col] == 2:
                    queue.append((row, col, 0))
                    visited[row][col] = True

        if freshOranges == 0:
            return 0

        maxMinutes = 0
        while queue:
            row, col, minutes = queue.pop(0)
            maxMinutes = max(maxMinutes, minutes)
            for r, c in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
                if 0 <= r < m and  0 <= c < n and grid[r][c] == 1 and not visited[r][c]:
                    visited[r][c] = True
                    queue.append((r, c, minutes+1))
                    freshOranges -= 1

        return -1 if freshOranges else maxMinutes
