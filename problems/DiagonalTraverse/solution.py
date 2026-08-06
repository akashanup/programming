class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
            Intuition:  The sum of indexes of each diagonal is same.
            [
                  0  1   2    3
                0[1, 2,  3,   4],
                1[5, 6,  7,   8],
                2[9, 10, 11, 12]
            ]
            First Diagonal: ((0,0)) => Sum = 0
            Second Diagonal: ((0,1), (1,0)) => Sum = 1
            Third Diagonal: ((0,2), (1,1), (2,0)) => Sum = 2
            Fourth Diagonal: ((0,3), (1,2), (2,1)) => Sum = 3
            Fifth Diagonal: ((1,3), (2,2)) => Sum = 4
            Sixth Diagonal: ((2,3)) => Sum = 5

            Keeping the above intuition in mind let's save all the elements for a particular sum of indexes ranges between 0 to (m-1) + (n-1) into a 2D list.
            Then sequentially iterate the items of hashmap in initial order and reverse order alternatively.
        """
        m = len(mat)
        n = len(mat[0])
        hash = [[] for _ in range((m + n - 2) + 1)]

        for r in range(m):
            for c in range(n):
                hash[r+c].append(mat[r][c])

        output = []
        i = 0
        while i <= m + n - 2:
            output += hash[i] if i % 2 else hash[i][::-1]
            i += 1

        return output
