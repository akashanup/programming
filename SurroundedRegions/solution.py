from collections import deque


class Solution:
    def updateConnectedFlippables(self, board, m, n, row, col, cantBeFlipped):
        queue = deque([(row, col)])
        connected = set()
        connected.add((row, col))
        minRow, maxRow = row, row
        minCol, maxCol = col, col
        while queue:
            row, col = queue.popleft()
            for r, c in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
                if 0 <= r < m and 0 <= c < n and board[r][c] == "O" and (r, c) not in connected:
                    connected.add((r, c))
                    queue.append((r, c))
                    minRow = min(minRow, r)
                    maxRow = max(maxRow, r)
                    minCol = min(minCol, c)
                    maxCol = max(maxCol, c)

        if minRow == 0 or maxRow == m - 1 or minCol == 0 or maxCol == n - 1:
            cantBeFlipped.union(connected)
        else:

            for r, c in connected:
                board[r][c] = "X"

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cantBeFlipped = set()
        m = len(board)
        n = len(board[0])
        for row in range(1, m - 1):
            for col in range(1, n - 1):
                if board[row][col] == "O" and (row, col) not in cantBeFlipped:
                    self.updateConnectedFlippables(board, m, n, row, col, cantBeFlipped)
