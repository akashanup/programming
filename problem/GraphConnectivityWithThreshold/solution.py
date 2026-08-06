class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for vertex in range(1, vertices + 1):
            self.parent[vertex] = vertex
            self.rank[vertex] = 0

    def find(self, vertex):
        # Path compression
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        parent1 = self.find(vertex1)
        parent2 = self.find(vertex2)
        # Union By Rank
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent2] > self.rank[parent1]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += 1


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        disjointSet = DisjointSet(n)
        for i in range(threshold + 1, n + 1):
            m = 1
            while i * m <= n:
                disjointSet.union(i, i * m)
                m += 1
        return [disjointSet.find(vertex1) == disjointSet.find(vertex2) for vertex1, vertex2 in queries]
