class Solution:
    def dpFn(self, cost, lastStep, lookup):
        if lastStep <= 1:
            return 0
        if lastStep not in lookup:
            oneStep = cost[lastStep - 1] + self.dpFn(cost, lastStep - 1, lookup)
            twoStep = cost[lastStep - 2] + self.dpFn(cost, lastStep - 2, lookup)
            lookup[lastStep] = min(oneStep, twoStep)
        return lookup[lastStep]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.dpFn(cost, len(cost), {})
