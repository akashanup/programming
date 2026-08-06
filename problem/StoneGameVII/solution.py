class Solution:
    def dpFn(self, stones, total, left, right, dp):
        if dp[left][right] is None:
            if right == left:
                dp[left][right] = 0
            if right - left == 1:
                dp[left][right] = max(stones[left], stones[right])
            if left < right:
                leftRemovedAliceScore = total - stones[left]
                bobScoreAfterAliceRemovedLeft = self.dpFn(stones, leftRemovedAliceScore, left + 1, right, dp)
                rightRemovedAliceScore = total - stones[right]
                bobScoreAfterAliceRemovedRight = self.dpFn(stones, rightRemovedAliceScore, left, right - 1, dp)
                dp[left][right] = max(leftRemovedAliceScore - bobScoreAfterAliceRemovedLeft,
                                      rightRemovedAliceScore - bobScoreAfterAliceRemovedRight)
        return dp[left][right]

    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[None] * n for _ in range(n)]
        return self.dpFn(stones, sum(stones), 0, len(stones) - 1, dp)
