class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1Len, word2Len = len(word1), len(word2)
    
        # Assume word1 is bigger than word2. If not then swap.
        if word1Len < word2Len: 
            word1, word2, word1Len, word2Len = word2, word1, word2Len, word1Len

        #Store solutions of sub problems.(DP approach)
        last, curr = [0] * (word2Len + 1), [0] * (word2Len + 1)

        for character in word1:
            for j in range(word2Len):
                curr[j + 1] = last[j] + 1 if character == word2[j] else max(curr[j], last[j + 1])
            last, curr = curr, last
        return word1Len + word2Len - (2 * last[word2Len])
