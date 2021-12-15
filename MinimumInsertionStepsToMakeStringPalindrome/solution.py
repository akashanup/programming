class Solution:
    def minInsertions(self, s: str, lookup={}) -> int:
        if len(s) <= 1:
            return 0
        if s not in lookup:
            if s[0] == s[-1]:
                lookup[s] = self.minInsertions(s[1:-1], lookup)
            else:
                lookup[s] = 1 + min(self.minInsertions(s[1:], lookup), self.minInsertions(s[:-1], lookup))
        return lookup[s]
