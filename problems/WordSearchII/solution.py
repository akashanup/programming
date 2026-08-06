"""
The idea is to first build a trie from given list of words.
Then for each cell of the board, check whether a word from words can be formed using the board traversal in horizontal or vertical direction. This can be achieved using backtracking.
"""


class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def insert(self, word: str) -> None:
        p = self.root
        for w in word:
            # If current char is not present
            if w not in p.children:
                p.children[w] = self.getNode()
            p = p.children[w]
        p.endOfWord = True


class Solution:

    def wordSearch(self, board, m, n, root, row, col, path, output):
        # word found!
        if root.endOfWord:
            output.append(path)
            root.endOfWord = False
        # pointers became out of range of board
        if row < 0 or row >= m or col < 0 or col >= n:
            return False
        if not root:
            return False

        temp = board[row][col]
        if not temp or temp not in root.children:
            return False
        root = root.children[temp]
        # Set the current cell to None so that we can keep track of the visited cell.
        board[row][col] = '#'
        for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            self.wordSearch(board, m, n, root, row + x, col + y, path + temp, output)
        # Backtrack
        board[row][col] = temp

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        # Insert each word into Trie
        trie = Trie()
        root = trie.root
        for word in words:
            trie.insert(word)

        output = []
        for row in range(m):
            for col in range(n):
                self.wordSearch(board, m, n, root, row, col, "", output)
        return output
