class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subBoxes = [[], [], [], [], [], [], [], [], []]
        for row in range(9):
            column = []
            for col in range(9):
                if board[row].count(str(col + 1)) > 1:
                    return False
                if board[col][row] in column:
                    return False
                else:
                    if board[col][row] != '.':
                        column.append(board[col][row])
                if row < 3:
                    if col < 3:
                        if board[row][col] in subBoxes[0]:
                            return False
                        else:
                            if board[row][col] != '.':
                                subBoxes[0].append(board[row][col])
                    elif col < 6:
                        if board[row][col] in subBoxes[1]:
                            return False
                        else:
                            if board[row][col] != '.':
                                subBoxes[1].append(board[row][col])
                    else:
                        if board[row][col] in subBoxes[2]:
                            return False
                        else:
                            if board[row][col] != '.':
                                subBoxes[2].append(board[row][col])
                elif row < 6:
                    if col < 3:
                        if board[row][col] in subBoxes[3]:
                            return False
                        else:
                            if board[row][col] != '.':
                                subBoxes[3].append(board[row][col])
                    elif col < 6:
                        if board[row][col] in subBoxes[4]:
                            return False
                        else:
                            if board[row][col] != '.':
                                subBoxes[4].append(board[row][col])
                    else:
                        if board[row][col] in subBoxes[5]:
                            return False
                        else:
                            if board[row][col] != '.':
                                subBoxes[5].append(board[row][col])
                else:
                    if col < 3:
                        if board[row][col] in subBoxes[6]:
                            return False
                        else:
                            if board[row][col] != '.':
                                subBoxes[6].append(board[row][col])
                    elif col < 6:
                        if board[row][col] in subBoxes[7]:
                            return False
                        else:
                            if board[row][col] != '.':
                                subBoxes[7].append(board[row][col])
                    else:
                        if board[row][col] in subBoxes[8]:
                            return False
                        else:
                            if board[row][col] != '.':
                                subBoxes[8].append(board[row][col])
        return True
