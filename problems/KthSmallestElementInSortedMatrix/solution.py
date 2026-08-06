from sortedcontainers import SortedList


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        n = len(matrix)
        sortedList = SortedList([])

        for row in range(n):
            sortedList += matrix[row]

        return sortedList[k - 1]


print(Solution().kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
print(Solution().kthSmallest(matrix=[[-5]], k=1))
