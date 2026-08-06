class Solution:
    def palindromePairs(self, words):
        wordsLen = len(words)
        palindromes = []
        for i, word in enumerate(words):
            for j in range(i + 1, wordsLen):
                w = word + words[j]
                if w == w[::-1]:
                    palindromes.append([i, j])
                w = words[j] + word
                if w == w[::-1]:
                    palindromes.append([j, i])
        return palindromes
