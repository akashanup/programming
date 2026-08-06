class Solution:
    EMPTY = "."
    KNIGHT = "K"

    def nKnights(self, n):
        board = self.__createBoard(n)
        answers = []
        self.__placeKnights(board, n, answers, 0, 0)
        return answers

    def __createBoard(self, n):
        return [[Solution.EMPTY for _ in range(n)] for _ in range(n)]

    def __placeKnights(self, board, n, answers, row, col):
        if n == 0:
            answers.append([[board[i][j] for j in range(len(board))] for i in range(len(board))])
        else:
            if row == len(board)-1 and col == len(board):
                return
            elif col == len(board):
                self.__placeKnights(board, n, answers, row + 1, 0)
            else:
                if self.__isSafe(board, row, col):
                    board[row][col] = Solution.KNIGHT
                    self.__placeKnights(board, n - 1, answers, row, col+1)
                    board[row][col] = Solution.EMPTY
                self.__placeKnights(board, n, answers, row, col + 1)

    def __isSafe(self, board, row, col):
        if self.__isValidCell(board, row + 2, col + 1) and board[row + 2][col + 1] == Solution.KNIGHT:
            return False
        if self.__isValidCell(board, row + 2, col - 1) and board[row + 2][col - 1] == Solution.KNIGHT:
            return False
        if self.__isValidCell(board, row + 1, col + 2) and board[row + 1][col + 2] == Solution.KNIGHT:
            return False
        if self.__isValidCell(board, row + 1, col - 2) and board[row + 1][col - 2] == Solution.KNIGHT:
            return False
        if self.__isValidCell(board, row - 2, col + 1) and board[row - 2][col + 1] == Solution.KNIGHT:
            return False
        if self.__isValidCell(board, row - 2, col - 1) and board[row - 2][col - 1] == Solution.KNIGHT:
            return False
        if self.__isValidCell(board, row - 1, col + 2) and board[row - 1][col + 2] == Solution.KNIGHT:
            return False
        if self.__isValidCell(board, row - 1, col - 2) and board[row - 1][col - 2] == Solution.KNIGHT:
            return False
        return True

    def __isValidCell(self, board, row, col):
        return 0 <= row < len(board) and 0 <= col < len(board)


n = 4
answers = Solution().nKnights(n)
for answer in answers:
    for i in range(len(answer)):
        for j in range(len(answer)):
            print(answer[i][j], end=" ")
        print()
    print()
