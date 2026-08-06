import sys


class Solution:
    def __dfs(self, grid, moves, row, col, lookup):
        if row == len(grid)-1:
            return grid[row][col]
        if (row, col) not in lookup:
            minCost = sys.maxsize
            for c in range(len(grid[row])):
                minCost = min(minCost, grid[row][col] + moves[grid[row][col]][c] + self.__dfs(grid, moves, row+1, c, lookup))
            lookup[(row, col)] = minCost
        return lookup[(row, col)]

    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        lookup = {}
        minCost = sys.maxsize
        row = 0
        for col in range(len(grid[row])):
            minCost = min(minCost, self.__dfs(grid, moveCost, row, col, lookup))
        return minCost