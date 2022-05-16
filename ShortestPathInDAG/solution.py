import sys


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = {_: [] for _ in range(V)}
        self.visited = [False] * V
        self.postVisit = []

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])

    def topologicalSort(self, node):
        self.visited[node] = True
        if self.graph[node]:
            for u, _ in self.graph[node]:
                if not self.visited[u]:
                    self.topologicalSort(u)
        self.postVisit.append(node)

    def shortestPath(self, node):
        print(self.graph)
        for u in range(self.V):
            if not self.visited[u]:
                self.topologicalSort(u)

        print(self.postVisit)
        distance = [sys.maxsize] * self.V
        distance[node] = 0

        while self.postVisit:
            u = self.postVisit.pop()

            for v, w in self.graph[u]:
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w

        return distance


gp = Graph(6)
gp.addEdge(0, 1, 5)
gp.addEdge(0, 2, 3)
gp.addEdge(1, 3, 6)
gp.addEdge(1, 2, 2)
gp.addEdge(2, 4, 4)
gp.addEdge(2, 5, 2)
gp.addEdge(2, 3, 7)
gp.addEdge(3, 4, -1)
gp.addEdge(4, 5, -2)
print(gp.shortestPath(1))
