class Solution:
    def dp(self, w1, w2, i, j, lookup):
        if (i, j) not in lookup:
            if i == len(w1) and j == len(w2):
                lookup[(i, j)] = 0
            elif i == len(w1):
                lookup[(i, j)] = len(w2)-j
            elif j == len(w2):
                lookup[(i, j)] = len(w1)-i
            elif w1[i] == w2[j]:
                lookup[(i, j)] = self.dp(w1, w2, i+1, j+1, lookup)
            else:
                lookup[(i, j)] = min(1+self.dp(w1, w2, i, j+1, lookup), 1+self.dp(w1, w2, i+1, j, lookup))
        return lookup[(i, j)]

    def minDistance(self, word1: str, word2: str) -> int:
        return self.dp(word1, word2, 0, 0, {})
