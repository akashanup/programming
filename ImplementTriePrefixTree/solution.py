class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        p = self.root
        for w in word:
            index = self._charToIndex(w)
            # If current char is not present
            if not p.children[index]:
                p.children[index] = self.getNode()
            p = p.children[index]
        p.endOfWord = True

    def search(self, word: str) -> bool:
        p = self.root
        for w in word:
            index = self._charToIndex(w)
            # If current char is not present
            if not p.children[index]:
                return False
            p = p.children[index]
        return p.endOfWord

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for w in prefix:
            index = self._charToIndex(w)
            # If current char is not present
            if not p.children[index]:
                return False
            p = p.children[index]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
