class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)

        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        maxH = 0
        maxV = 0
        for i in range(1, len(horizontalCuts)):
            maxH = max(maxH, horizontalCuts[i] - horizontalCuts[i-1])

        for j in range(1, len(verticalCuts)):
            maxV = max(maxV, verticalCuts[j] - verticalCuts[j-1])
        return (maxH * maxV) % (10**9 + 7)
