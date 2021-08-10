class Solution:
    def dpFn(self, wordList, word, lookup, map):
        if word not in lookup:
            exists = False
            if word == '':
                exists = True
            else:
                for i in range(1, len(word) + 1):
                    if word[:i] in wordList and self.dpFn(wordList, word[i:], lookup, map):
                        exists = True
                        if len(word[i:]):
                            map[word] = [[word[:i]] + [word[i:]]]
                            if word[:i] in map:
                                for w in map[word[:i]]:
                                    map[word].append(w + [word[i:]])
                            if word[i:] in map:
                                for w in map[word[i:]]:
                                    map[word].append([word[:i]] + w)
                        break
            lookup[word] = exists
        return lookup[word]

    def wordBreak(self, wordList):
        map = {}
        for word in wordList:
            self.dpFn(wordList, word, {}, map)
        return map


wordList = ["happy", "rise", "for", "set", "sunrise", "su", "nset", "sunset", "mind", "happymind", "n", "rise", "happysunrise"]
print(Solution().wordBreak(wordList))
