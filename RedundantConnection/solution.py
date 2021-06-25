class Graph:
    def __init__(self, vertices):
        self.parent = list(range(vertices))

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertexX, vertexY):
        x = self.find(vertexX)
        y = self.find(vertexY)
        self.parent[x] = y


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = Graph(len(edges))
        for i, j in edges:
            if graph.find(i-1) == graph.find(j-1):
                return [i, j]
            else:
                graph.union(i-1, j-1)
