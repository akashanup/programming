class Solution:
    def dp(self, s, wordDict, index, lookup):
        if index >= len(s):
            return True
        if lookup[index] == -1:
            if s[index:] in wordDict:
                lookup[index] = True
            else:
                found = False
                i = index+1
                while i < len(s):
                    if s[index:i] in wordDict and self.dp(s, wordDict, i, lookup):
                        found = True
                        break
                    i += 1
                lookup[index] = found
        return lookup[index]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dp(s, set(wordDict), 0, [-1 for i in range(len(s))])
