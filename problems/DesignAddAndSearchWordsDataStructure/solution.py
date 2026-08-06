class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = self.getTrieNode()

    def getTrieNode(self):
        return TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = self.getTrieNode()
            node = node.children[ch]
        node.endOfWord = True

    def search(self, word: str, node=None) -> bool:
        if not node:
            node = self.root
        for index,ch in enumerate(word):
            if ch == '.':
                for child in node.children:
                    if self.search(word[index+1:], node.children[child]):
                        return True
                return False
            elif ch not in node.children:
                return False
            node = node.children[ch]
        return node.endOfWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
