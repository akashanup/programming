class Solution:
    EMPTY = "."
    NUMBERS = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

    def solveSudoku(self, board):
        if self.__placeNumbers(board, 1):
            return board
        return -1

    def __placeNumbers(self, board, num):
        row, col = self.__nextEmptyCell(board)
        if row is None:
            return True
        if num > 9:
            return False
        ans = None
        if self.__isValid(board, row, col, Solution.NUMBERS[num]):
            board[row][col] = Solution.NUMBERS[num]
            if self.__placeNumbers(board, 1):
                return True
            board[row][col] = Solution.EMPTY
        return self.__placeNumbers(board, num + 1)

    def __nextEmptyCell(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == Solution.EMPTY:
                    return row, col
        return None, None

    def __isValid(self, board, row, col, item):
        # Check for row
        for c in range(len(board)):
            if board[row][c] == item:
                return False
        # Check for col
        for r in range(len(board)):
            if board[r][col] == item:
                return False
        # Check for block
        r, c = (row // 3) * 3, (col // 3) * 3
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if board[i][j] == item:
                    return False
        return True


"""
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [
["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:
"""
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().solveSudoku(board))

