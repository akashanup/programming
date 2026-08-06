class Solution:
    def isAnyLetterCommon(self, minLenStr, maxLenStr):
        minLenStr, maxLenStr = (minLenStr, maxLenStr) if len(minLenStr) <= len(maxLenStr) else (maxLenStr, minLenStr)
        for i in minLenStr:
            if i in maxLenStr:
                return False
        return True

    def maxProduct(self, words: List[str]) -> int:
        wordsLen = len(words)
        maxProd = 0
        for i in range(wordsLen - 1):
            for j in range(i+1, wordsLen):
                if self.isAnyLetterCommon(words[i], words[j]):
                    maxProd = max(maxProd, len(words[i]) * len(words[j]))
        return maxProd
