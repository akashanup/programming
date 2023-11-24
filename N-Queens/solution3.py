class Solution:
    EMPTY = "."
    QUEEN = "Q"

    def nQueens(self, n):
        board = self.__createBoard(n)
        return self.__placeQueens(board, n, 0, 0)

    def __createBoard(self, n):
        return [[Solution.EMPTY for _ in range(n)] for _ in range(n)]

    def __placeQueens(self, board, n, row, col):
        if n == 0:
            return [[[board[i][j] for j in range(len(board))] for i in range(len(board))]]
        else:
            if row == len(board)-1 and col == len(board):
                return []
            elif col == len(board):
                return self.__placeQueens(board, n, row + 1, 0)
            else:
                answers = []
                if self.__isSafe(board, row, col):
                    board[row][col] = Solution.QUEEN
                    answers += self.__placeQueens(board, n - 1, row, col+1)
                    board[row][col] = Solution.EMPTY
                answers += self.__placeQueens(board, n, row, col + 1)
                return answers

    def __isSafe(self, board, row, col):
        # Check for column
        for r in range(row):
            if board[r][col] == Solution.QUEEN:
                return False
        # Check for row
        for c in range(col):
            if board[row][c] == Solution.QUEEN:
                return False
        # Check for left diagonal
        r, c = row, col
        while r >= 0 and c >= 0:
            if board[r][c] == Solution.QUEEN:
                return False
            r -= 1
            c -= 1
        # Check for right diagonal
        r, c = row, col
        while r >= 0 and c < len(board):
            if board[r][c] == Solution.QUEEN:
                return False
            r -= 1
            c += 1
        return True


n = 4
answers = Solution().nQueens(n)
for answer in answers:
    for i in range(len(answer)):
        for j in range(len(answer)):
            print(answer[i][j], end=" ")
        print()
    print()
