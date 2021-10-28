class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        """
            Since we don't have a straight forward base case to find the nearest zero for any cell, so to solve this type of questions, reverse engineering is required.
            The idea is to first keep a track of all the elements having zeros in a queue and then use BFS to update the value of nearest zero for its neighbours.
            Since BFS is used, so once a value for any element is found, the values for its neighbours would also be found.
        """

        visited = [[None for _ in range(n)] for _ in range(m)]
        queue = []
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row,col))
                    visited[row][col] = True


        while queue:
            row, col = queue.pop(0)
            for r, c in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
                if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                    visited[r][c] = True
                    mat[r][c] = 1 + mat[row][col]
                    queue.append((r, c))
        return mat
