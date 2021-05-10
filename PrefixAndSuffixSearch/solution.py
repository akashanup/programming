class WordFilter:

    def __init__(self, words: List[str]):
        self.table = {}
        for index,word in enumerate(words):
            lenWord = len(word)
            prefixes = [word[:i] for i in range(lenWord + 1)]
            suffixes = [word[lenWord - i:] for i in range(lenWord + 1)]
            
            for prefix in prefixes:
                for suffix in suffixes:
                    self.table[prefix + "#" + suffix] = index

    def f(self, prefix: str, suffix: str) -> int:
        key = prefix + "#" + suffix
        return self.table[key] if key in self.table else -1
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)