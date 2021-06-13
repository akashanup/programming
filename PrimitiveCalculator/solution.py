import sys


class Solution:
    def dpFn(self, n, lookup):
        if lookup[n] == -1:
            minOperation = sys.maxsize
            if n - 1 >= 1:
                minOperation = min(minOperation, 1 + self.dpFn(n - 1, lookup))
            if n % 2 == 0 and n // 2 >= 1:
                minOperation = min(minOperation, 1 + self.dpFn(n // 2, lookup))
            if n % 3 == 0 and n // 3 >= 1:
                minOperation = min(minOperation, 1 + self.dpFn(n // 3, lookup))
            lookup[n] = minOperation
        return lookup[n]

    def optimalSequence(self, n):
        lookup = [-1] * (n + 1)
        lookup[1] = 0
        self.dpFn(n, lookup)
        ptr = n
        sequence = [ptr]
        while ptr >= 1:
            candidates = [ptr - 1]
            if ptr % 2 == 0:
                candidates.append(ptr // 2)
            if ptr % 3 == 0:
                candidates.append(ptr // 3)
            ptr = min([(c, lookup[c]) for c in candidates], key=lambda x: x[1])[0]
            sequence.append(ptr)
        sequence = sequence[:-1]
        sequence = sequence[::-1]
        return sequence
