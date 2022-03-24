"""
Logic: Used the fact that the value of any row, col of a pascal's triange is rowCcol i.e row! / (col! * (row-col)!)
"""


class Solution:
    def fact(self, num, factorial):
        if num not in factorial:
            ans = 1
            for i in range(2, num+1):
                ans *= i
            factorial[num] = ans
        return factorial[num]

    def generate(self, numRows: int) -> List[List[int]]:
        """
            For n = 5, Pascal's Triangle:
                 1
                1 1
               1 2 1
              1 3 3 1
             1 4 6 4 1
        """
        factorial = {0:1, 1:1}
        pascalsTriangle = [None]*numRows
        for row in range(numRows):
            current = [None]*(row+1)
            for col in range(row+1):
                current[col] = self.fact(row, factorial) // (self.fact(col, factorial) * self.fact(row-col, factorial))
            pascalsTriangle[row] = current
        return pascalsTriangle
