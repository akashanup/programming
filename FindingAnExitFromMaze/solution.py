class Solution:
    def explore(self, graph, u, v, visited):
        visited[u] = True
        if u == v:
            return 1
        for node in graph[u]:
            if not visited[node]:
                if self.explore(graph, node, v, visited):
                    return 1
        return 0

    def canExit(self, n, edges, u, v):
        graph = {}
        visited = [None] * n
        for i in range(n):
            graph[i] = []

        for nodeU, nodeV in edges:
            graph[nodeU - 1].append(nodeV - 1)
            graph[nodeV - 1].append(nodeU - 1)

        return self.explore(graph, u - 1, v - 1, visited)


print(Solution().canExit(4, [[1, 2], [3, 2], [4, 3], [1, 4]], 1, 4))
print(Solution().canExit(4, [[1, 2], [3, 2]], 1, 4))


