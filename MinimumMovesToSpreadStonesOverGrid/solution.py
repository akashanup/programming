from typing import List
import sys


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        places, stones = [], {}
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    places.append((i, j))
                if grid[i][j] > 1:
                    stones[(i, j)] = grid[i][j]
        return self.__dfs(stones, places)

    def __dfs(self, stones, places):
        if len(places) == 0:
            return 0
        minMoves = sys.maxsize
        i1, j1 = places.pop()
        for (i2, j2) in stones.keys():
            if stones[(i2, j2)] > 1:
                stones[(i2, j2)] -= 1
                cost = abs(i2 - i1) + abs(j2 - j1)
                minMoves = min(minMoves, self.__dfs(stones, places) + cost)
                stones[(i2, j2)] += 1
        places.append((i1, j1))
        return minMoves