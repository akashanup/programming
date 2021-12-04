"""
Logic:
    The way to solve the problem is to notice that we always know the last character to match. That gives us an idea to build a trie of reversed words, and try to match the reversed stream of characters.
    This way, instead of multiple choices to match, we always have one path: to match character by character starting from the end of the stream. We could stop once we meet the "end of word" label, which means success. If we couldn't match a character before we meet that label, that means fail.
"""


class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = []
        self.trie = {}
        for word in set(words):
            node = self.trie
            for ch in word[::-1]:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = True

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        node = self.trie
        for i in range(len(self.letters)-1, -1, -1):
            if '$' in node:
                return True
            if self.letters[i] not in node:
                return False
            node = node[self.letters[i]]
        return '$' in node
