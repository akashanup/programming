class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if (m * n != r * c) or (m == r and n == c):
            return mat
        else:
            reshapeMat = [[None for j in range(c)] for i in range(r)]
            a = 0
            b = 0
            for i in range(r):
                for j in range(c):
                    reshapeMat[i][j] = mat[a][b]
                    b += 1
                    if b == n:
                        a += 1
                        b = 0
            return reshapeMat
