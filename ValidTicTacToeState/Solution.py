class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        countX = 0
        countO = 0
        for row in range(3):
            countX += board[row].count('X')
            countO += board[row].count('O')
            board[row] = [i for i in board[row]]
        if 0 <= countX - countO <= 1:
            xWins = False
            oWins = False
            # Check row wise
            for row in range(3):
                # Check for diagonal
                if not xWins:
                    xWins = True if board[row].count('X') == 3 else False
                if not oWins:
                    oWins = True if board[row].count('O') == 3 else False
            # Check column wise
            for col in range(3):
                if not xWins:
                    xWins = True if [board[0][col], board[1][col], board[2][col]].count('X') == 3 else False
                if not oWins:
                    oWins = True if [board[0][col], board[1][col], board[2][col]].count('O') == 3 else False
            # Check diagonals
            if not xWins:
                xWins = ('X' == board[0][0] == board[1][1] == board[2][2]) or ('X' == board[0][2] == board[1][1] == board[2][0])
            if not oWins:
                oWins = ('O' == board[0][0] == board[1][1] == board[2][2]) or ('O' == board[0][2] == board[1][1] == board[2][0])
            # Return False if both wins
            if xWins and oWins:
                return False
            if xWins and countX == countO:
                return False
            if oWins and countX > countO:
                return False
            return True
        else:
            return False
