class Solution:
    def calculateNumberOfWaysToMoveOut(self, m, n, startRow, startColumn):
        ways = 0
        if startRow == 0:
            ways += 1
        if startRow == m - 1:
            ways += 1
        if startColumn == 0:
            ways += 1
        if startColumn == n - 1:
            ways += 1
        return ways

    def dpFn(self, m, n, maxMove, startRow, startColumn, count, lookup):
        key = (maxMove, startRow, startColumn)
        if key not in lookup:
            if maxMove == 0:
                lookup[key] = 0
            else:
                count += self.calculateNumberOfWaysToMoveOut(m, n, startRow, startColumn)
                if maxMove > 1:
                    # There are at least two moves left, one of which will be taken to to move into any direction and the next could be taken to move out.
                    # Forward
                    if startColumn < n - 1:
                        count += self.dpFn(m, n, maxMove - 1, startRow, startColumn + 1, 0, lookup)
                    # Backward
                    if startColumn > 0:
                        count += self.dpFn(m, n, maxMove - 1, startRow, startColumn - 1, 0, lookup)
                    # Upward
                    if startRow > 0:
                        count += self.dpFn(m, n, maxMove - 1, startRow - 1, startColumn, 0, lookup)
                    # Downward
                    if startRow < m - 1:
                        count += self.dpFn(m, n, maxMove - 1, startRow + 1, startColumn, 0, lookup)
                lookup[key] = (count % ((10 ** 9) + 7))
        return lookup[key]

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return self.dpFn(m, n, maxMove, startRow, startColumn, 0, {})
