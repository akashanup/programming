class Solution:
    def subMatrixSumQueries(self, matrix, tli, tlj, rbi, rbj):
        for row in range(len(matrix)):
            # aux[row][0] = matrix[row][0]
            for col in range(1, len(matrix[0])):
                matrix[row][col] = matrix[row][col] + matrix[row][col - 1]
        print(matrix)
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] += matrix[row - 1][col]
        """ 
            Sub matrix sum:
                matrix[rbi][rbj] - matrix[rbi][tlj-1] - matrix[tli-1][rbj] + matrix[tli-1][tlj-1]
        """
        return matrix[rbi][rbj] - matrix[rbi][tlj-1] - matrix[tli-1][rbj] + matrix[tli-1][tlj-1]


print(Solution().subMatrixSumQueries([[1, 2, 3, 4, 6], [5, 3, 8, 1, 2], [4, 6, 7, 5, 5], [2, 4, 8, 9, 4]], tli=2, tlj=2,
                                     rbi=3, rbj=4))
