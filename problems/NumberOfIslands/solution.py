class Solution:
    DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        island = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    island += 1
                    queue = [(row, col)]
                    # Mark it visited
                    grid[row][col] = "0"
                    # Recur for all its neighbours having "1" and mark them as visited
                    while queue:
                        current = queue.pop(0)
                        for direction in Solution.DIRECTIONS:
                            newRow = current[0] + direction[0]
                            newCol = current[1] + direction[1]
                            if 0 <= newRow < n and 0 <= newCol < m and grid[newRow][newCol] == "1":
                                queue.append((newRow, newCol))
                                grid[newRow][newCol] = "0"
        return island
