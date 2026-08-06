"""
Logic:
    This problem is very similar to 300. Longest Increasing Subsequence
    So we will use a similar logic for dp to check whether any element has a predecessor before its index or not and update its dp array value accordingly.
"""


class Solution:
    def isPredecessor(self, w1, w2):
        if len(w2) != len(w1)+1:
            return False
        i, j = 0, 0
        while j < len(w2):
            if i < len(w1) and w1[i] == w2[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(w1) and j == len(w2)

    def longestStrChain(self, words: List[str]) -> int:
        dp = [1] * len(words)
        words.sort(key=len)
        for i in range(len(words)):
            for j in range(i):
                if self.isPredecessor(words[j], words[i]) and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
        return max(dp)
