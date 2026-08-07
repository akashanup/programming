class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lookup = [[1] for i in range(numRows)]
        for i in range(1, numRows):
            for j in range(1, i):
                lookup[i].append(lookup[i - 1][j - 1] + lookup[i - 1][j])
            lookup[i].append(1)
        return lookup
