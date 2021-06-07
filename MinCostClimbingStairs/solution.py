class Solution:
    def dpFn(self, cost, lastStep, lookup):
        if lastStep <= 1:
            return 0
        if lastStep not in lookup:
            oneStep = cost[lastStep - 1] + self.dpFn(cost, lastStep - 1, lookup)
            twoStep = cost[lastStep - 2] + self.dpFn(cost, lastStep - 2, lookup)
            lookup[lastStep] = min(oneStep, twoStep)
        return lookup[lastStep]

    def minCostClimbingStairs(self, cost):
        # Bottom-Up DP (Tabulation)
        return self.dpFn(cost, len(cost), {})

        # Top-Down DP (Memoization)
        # totalCost = [None] * (len(cost) + 1)
        # totalCost[0] = 0
        # totalCost[1] = 0
        # i = 2
        # while i <= len(cost):
        #     oneStep = cost[i - 1] + totalCost[i - 1]
        #     twoStep = cost[i - 2] + totalCost[i - 2]
        #     totalCost[i] = min(oneStep, twoStep)
        #     i += 1
        # return totalCost[-1]
