class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, - 1], [1, 1], [1, -1], [-1, 1]]
        for direction in directions:
            x = rMove + direction[0]
            y = cMove + direction[1]
            goodLine = False
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == color and (
                        abs(x - rMove) >= 2 or abs(y - cMove) >= 2):
                    goodLine = True
                    break
                if board[x][y] == color or board[x][y] == ".":
                    break
                x += direction[0]
                y += direction[1]
            if goodLine:
                return True
        return False
