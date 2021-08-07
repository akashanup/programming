class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        cuts = [x for x in range(-1, len(s))]
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[i:j] == s[j:i:-1]:
                    cuts[j + 1] = min(cuts[j + 1], cuts[i] + 1)
        return cuts[-1]
