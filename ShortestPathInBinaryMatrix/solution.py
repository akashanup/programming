from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([[0, 0, 1]])
        while queue:
            r, c, pathLength = queue.popleft()
            if grid[r][c] == 0:
                if r == len(grid)-1 and c == len(grid[0])-1:
                    return pathLength

                grid[r][c] = 1

                for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
                    if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]) and grid[r+dr][c+dc] == 0:
                        queue.append([r+dr, c+dc, pathLength+1])

        return -1
