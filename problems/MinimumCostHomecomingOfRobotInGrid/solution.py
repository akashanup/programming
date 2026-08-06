class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        cost = 0
        """
        Since the robot can't walk in the diagonals hence whhatever path the robot takes, 
        it has to cover all the intermediate rows and columns.
        Hence just calculate the cost for taking all the intermediate rows anc columns and that would be the minimum cost.
        """
        r1, r2 = startPos[0], homePos[0]
        c1, c2 = startPos[1], homePos[1]
        if r1 < r2:
            for r in range(r1+1, r2+1):
                cost += rowCosts[r]
        else:
            for r in range(r1-1, r2-1, -1):
                cost += rowCosts[r]
        if c1 < c2:
            for c in range(c1+1, c2+1):
                cost += colCosts[c]
        else:
            for c in range(c1-1, c2-1, -1):
                cost += colCosts[c]
        return cost