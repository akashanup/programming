class Solution:
    def dpFn(self, W, w, v, n, lookup):
        if lookup[W] == -1:
            lookup[W] = 0
            for i in range(n):
                lookup[W] = max(lookup[W], v[i] + self.dpFn(W - w[i], w, v, n, lookup) if W - w[i] >= 0 else lookup[W])
        return lookup[W]

    def maximumValue(self, W, w, v):
        return self.dpFn(W, w, v, len(w), [-1] * (W + 1))


print(Solution().maximumValue(100, [5, 10, 15], [10, 30, 20]))
print(Solution().maximumValue(8, [1, 3, 4, 5], [10, 40, 50, 70]))
print(Solution().maximumValue(100, [1, 50], [1, 30]))
