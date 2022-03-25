class Solution:
    """
        For n = 5, Pascal's Triangle:
             1
            1 1
           1 2 1
          1 3 3 1
         1 4 6 4 1
    """
    def waterOverflow(self, K, R, C):
        # Pascale Triangle structure
        glasses = [[0] * (row+1) for row in range(R)]
        glasses[0][0] = K
        for r in range(1, len(glasses)):
            for c in range(len(glasses[r])):
                if c == 0:
                    left = (glasses[r-1][0] - 1) / 2
                    glasses[r][c] = left if left > 0 else 0
                elif c == len(glasses[r]) - 1:
                    right = (glasses[r-1][-1] - 1) / 2
                    glasses[r][c] = right if right > 0 else 0
                else:
                    left = (glasses[r-1][c-1] - 1) / 2
                    right = (glasses[r-1][c] - 1) / 2
                    glasses[r][c] = (left if left > 0 else 0) + (right if right > 0 else 0)
        return "{0:.6f}".format(1 if glasses[R-1][C-1] >= 1 else glasses[R-1][C-1])


print(Solution().waterOverflow(6, 3, 3))
print(Solution().waterOverflow(65, 10, 3))
