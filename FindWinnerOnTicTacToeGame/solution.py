class Solution:
    def checkWinner(self, board, sign):
        winnerSequence = [sign] * 3
        for row in range(3):
            if winnerSequence == board[row]:
                return True
        for col in range(3):
            column = []
            for row in range(3):
                column.append(board[row][col])
            if winnerSequence == column:
                return True
        return (winnerSequence == [board[0][0], board[1][1], board[2][2]]) or (winnerSequence == [board[0][2], board[1][1], board[2][0]])

    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[None for _ in range(3)] for _ in range(3)]
        turnA = True
        for x, y in moves:
            if turnA:
                turnA = False
                board[x][y] = "A"
                if self.checkWinner(board, "A"):
                    return "A"
            else:
                turnA = True
                board[x][y] = "B"
                if self.checkWinner(board, "B"):
                    return "B"
        return "Draw" if len(moves) == 9 else "Pending"
