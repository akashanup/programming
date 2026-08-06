class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        lookup = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for s in text:
            if s in "balon":
                lookup[s] += 1
        count = 0
        while True:
            if lookup['b'] > 0 and lookup['a'] > 0 and lookup['l'] > 1 and lookup['o'] > 1 and lookup['n'] > 0:
                lookup['b'] -= 1
                lookup['a'] -= 1
                lookup['l'] -= 2
                lookup['o'] -= 2
                lookup['n'] -= 1
                count += 1
            else:
                break
        return count
