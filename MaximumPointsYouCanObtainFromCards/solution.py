class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N, i, j = len(cardPoints), 0, len(cardPoints) - k
        total = sum(cardPoints[j:])
        best = total
        for x in range(k):
            total += cardPoints[i] - cardPoints[j]
            best = max(best, total)
            i += 1
            j += 1
        return best