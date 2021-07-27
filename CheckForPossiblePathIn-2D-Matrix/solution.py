class Solution:
    def isPath(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = [[0, 0]]
        while queue:
            currentPos = queue.pop()
            if currentPos[0] == m - 1 and currentPos[1] == n - 1:
                return True
            # Mark current position as visited
            matrix[currentPos[0]][currentPos[1]] = -1
            # Move next to all possible places
            for direction in DIRECTIONS:
                nextPosX = currentPos[0] + direction[0]
                nextPosY = currentPos[1] + direction[1]
                if 0 <= nextPosX < m and 0 <= nextPosY < n and matrix[nextPosX][nextPosY] != -1:
                    queue.append([nextPosX, nextPosY])
        return False


'''
Alternative Solution:
def recur(matrix, r, c, m, n):
    print(r, c)
    if r == m - 1 and c == n - 1:
        return True
    matrix[r][c] = -1
    # Backward
    if r > 0 and matrix[r - 1][c] != -1:
        if recur(matrix, r - 1, c, m, n):
            return True
    # Forward
    if r < m - 1 and matrix[r + 1][c] != -1:
        if recur(matrix, r + 1, c, m, n):
            return True
    # Upward
    if c > 0 and matrix[r][c - 1] != -1:
        if recur(matrix, r, c - 1, m, n):
            return True
    # Downward
    if c < n - 1 and matrix[r][c + 1] != -1:
        if recur(matrix, r, c + 1, m, n):
            return True
    return False
'''
