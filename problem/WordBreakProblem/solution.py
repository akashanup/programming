class Solution:
    def dpFn(self, wordList, word, lookup):
        if word not in lookup:
            exists = False
            if word == '':
                exists = True
            else:
                for i in range(1, len(word) + 1):
                    if word[:i] in wordList and self.dpFn(wordList, word[i:], lookup):
                        exists = True
                        break
            lookup[word] = exists
        return lookup[word]

    def wordBreak(self, wordList, word):
        return self.dpFn(wordList, word, {})
