class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if self.rank[i] > self.rank[j]:
            self.parent[j] = i
        elif self.rank[j] > self.rank[i]:
            self.parent[i] = j
        else:
            self.parent[j] = i
            self.rank[i] += 1


class Solution:
    def canExit(self, n, edges, u, v):
        disjointSet = DisjointSet(n)

        for nodeU, nodeV in edges:
            i = disjointSet.find(nodeU - 1)
            j = disjointSet.find(nodeV - 1)
            if i != j:
                disjointSet.union(i, j)
        return 1 if disjointSet.find(u - 1) == disjointSet.find(v - 1) else 0


print(Solution().canExit(4, [[1, 2], [3, 2], [4, 3], [1, 4]], 1, 4))
print(Solution().canExit(4, [[1, 2], [3, 2]], 1, 4))
