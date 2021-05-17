class Solution:
    def getChainCount(self, words, word, chainCount, predecessorCountDict):
        if word in words:
            chainCount += 1
            if word not in predecessorCountDict:
                predecessorCount = [0] * len(word)
                for key, letter in enumerate(word):
                    predecessor = word[:key] + word[key + 1:]
                    if predecessor:
                        predecessorCount[key] = self.getChainCount(words, predecessor, 0, predecessorCountDict)
                predecessorCountDict[word] = max(predecessorCount)
            chainCount += predecessorCountDict[word]
        return chainCount

    def longestStrChain(self, words: List[str]) -> int:
        chainCount = [0] * len(words)
        for key, word in enumerate(words):
            chainCount[key] = self.getChainCount(words, word, 0, {})
        return max(chainCount)
