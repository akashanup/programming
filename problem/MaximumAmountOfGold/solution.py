class Solution:
    def dpFn(self, W, w, n, lookup):
        if lookup[W] == -1:
            if n == 0 or W == 0:
                lookup[W] = 0
            elif w[n - 1] > W:
                lookup[W] = self.dpFn(W, w, n - 1, lookup)
            else:
                lookup[W] = max((w[n - 1] + self.dpFn(W - w[n - 1], w, n - 1, lookup)), self.dpFn(W, w, n - 1, lookup))
        return lookup[W]

    def optimalWeight(self, W, w):
        n = len(w)
        lookup = [-1 for i in range(W + 1)]
        self.dpFn(W, w, n, lookup)
        return lookup[W]
