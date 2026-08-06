class TrieNode:
    def __init__(self):
        self.children = {}
        self.eof = False


class Trie:
    def __init__(self):
        self.root = self.__getTrieNode()

    def __getTrieNode(self):
        return TrieNode()

    def add(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = self.__getTrieNode()
            node = node.children[ch]
        node.eof = True

    def wordsStratsWith(self, prefix):
        words = []
        node = self.root
        count = 0
        for ch in prefix:
            if ch not in node.children:
                break
            count += 1
            node = node.children[ch]
        # If prefix is found, return all the words with the prefix in sorted order. Else return empty list.
        if len(prefix) == count:
            wordsFound = []
            self.__dfs(node, list(prefix), wordsFound)
            words += map(lambda word: "".join(word), wordsFound)
        return words

    def __dfs(self, node, word, words):
        if len(words) == 3:
            return
        if node.eof:
            words.append(word)
        children = sorted(node.children.keys())
        for ch in children:
            self.__dfs(node.children[ch], word + [ch], words)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.add(product)
        suggestions = []
        for i in range(len(searchWord)):
            suggestions.append(trie.wordsStratsWith(searchWord[:i + 1]))
        return suggestions
