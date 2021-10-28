class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        lookup = [[m+n for _ in range(n)] for _ in range(m)]
        """
            Since it is very hard to get to the base condition mat[row][col] == 0 every time so, lets go with worst scenario for every cell.
            1. Assign m+n to be the length for each cell to reach to the nearest zero.
            2. Traverse the matrix two times from top/left to bottom/right so that in the first traversal, previous rows/columns can be taken as base condition and in second traversal next rows/columns can be taken as base condition.
            In the first traversal, Start from the first cell and check for the nearest zero either in upward of backward direction.
            In the second traversal, Start from the last cell and check for the nearest zero either in downward of forward direction.
        """
        # Either moving up or left
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    lookup[row][col] = 0
                else:
                    if row > 0:
                        lookup[row][col] = min(lookup[row][col], 1 + lookup[row - 1][col])
                    if col > 0:
                        lookup[row][col] = min(lookup[row][col], 1 + lookup[row][col - 1])
        # Either moving down or right
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row < m - 1:
                    lookup[row][col] = min(lookup[row][col], 1 + lookup[row + 1][col])
                if col < n - 1:
                    lookup[row][col] = min(lookup[row][col], 1 + lookup[row][col + 1])
        return lookup
