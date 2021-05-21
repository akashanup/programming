class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        patternLettersStr = ''
        for letter in pattern:
            patternLettersStr += str(pattern.index(letter))
        result = []
        for word in words:
            wordLettersStr = ''
            for letter in word:
                wordLettersStr += str(word.index(letter))
            if patternLettersStr == wordLettersStr:
                result.append(word)
        return result
