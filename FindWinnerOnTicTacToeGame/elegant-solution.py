class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0, 0, 0]
        cols = [0, 0, 0]
        diagonal = 0
        antiDiagonal = 0
        """
            Let's say A's sign is 1 and B's sign is -1.
        """
        turnA = 1
        for row, col in moves:
            rows[row] += turnA
            cols[col] += turnA
            if row == col:
                diagonal += turnA
            if row + col == 2:
                antiDiagonal += turnA

            if abs(rows[row]) == 3 or abs(cols[col]) == 3 or abs(diagonal) == 3 or abs(antiDiagonal) == 3:
                return "A" if turnA == 1 else "B"
            turnA *= -1
        return "Draw" if len(moves) == 9 else "Pending"
