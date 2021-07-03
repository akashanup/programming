from itertools import accumulate, product, combinations
from sortedcontainers import SortedList


class Solution:
    def countRangeSum(self, row, k):
        sortedList, ans = SortedList([0]), -float("inf")
        for s in accumulate(row):
            idx = sortedList.bisect_left(s - k)
            if idx < len(sortedList):
                ans = max(ans, s - sortedList[idx])
            sortedList.add(s)
        return ans

    def maxSumSubmatrix(self, matrix, k):
        r = len(matrix)
        c = len(matrix[0])
        ans = -float("inf")

        for i, j in product(range(1, r), range(c)):
            matrix[i][j] += matrix[i-1][j]

        matrix = [[0] * c] + matrix

        for r1, r2 in combinations(range(r + 1), 2):
            row = [j - i for i, j in zip(matrix[r1], matrix[r2])]
            ans = max(ans, self.countRangeSum(row, k))

        return ans
