class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        substringCount = 0
        for word in words:
            substringCount += 1
            start = 0
            for w in word:
                index = s.find(w, start)
                if index != -1:
                    start = index + 1
                else:
                    substringCount -= 1
                    break
        return substringCount
