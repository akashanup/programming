class DisjointSet:
    def __init__(self, V):
        self.V = V
        self.graph = []
        self.rank = {}
        self.parent = {}

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def findParent(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.findParent(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        x = self.findParent(u)
        y = self.findParent(v)
        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1

    def KruskalMST(self):
        self.graph.sort(key=lambda x: x[2])
        i, edges, mst = 0, 0, []
        while edges < self.V - 1:
            u, v, w = self.graph[i]
            x = self.findParent(u)
            y = self.findParent(v)
            if x != y:
                edges += 1
                mst.append(self.graph[i])
                self.union(x, y)
            i += 1
        minCost = 0
        for u, v, w in mst:
            minCost += w
        return minCost


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        v = len(points)

        ds = DisjointSet(v)

        for i in range(len(points)):
            ds.parent[i] = i
            ds.rank[i] = 0

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                ds.addEdge(i, j, distance)

        return ds.KruskalMST()
