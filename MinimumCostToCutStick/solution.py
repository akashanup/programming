import sys


class Solution:
    def dp(self, start, end, cuts, lookup):
        key = (start, end)
        if key not in lookup:
            minCost = sys.maxsize
            # For a piece of stick, we have to analyze all the cuts to determine the minimum cost to cut.
            for cut in cuts:
                # If cut can be applied to the stick.
                if start < cut < end:
                    # Cost of cut would be => the length of stick + minimum cost of cuts for first piece of stick + minimum cost of cuts for second(last) piece of stick
                    minCost = min(minCost,
                                  end - start + self.dp(start, cut, cuts, lookup) + self.dp(cut, end, cuts, lookup))
                # If a stick couldn't be cut any further, the cost of cutting would be zero.
            lookup[key] = minCost if minCost != sys.maxsize else 0
        return lookup[key]

    def minCost(self, n: int, cuts: List[int]) -> int:
        return self.dp(0, n, cuts, {})
