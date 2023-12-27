class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost, prev = 0, 0
        for curr in range(1, len(colors)):
            if colors[prev] != colors[curr]:
                prev = curr
            else:
                cost += min(neededTime[prev], neededTime[curr])
                if neededTime[prev] < neededTime[curr]:
                    prev = curr
        return cost