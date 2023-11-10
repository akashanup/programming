class Solution:
    def dfs(self, graph, visited, node, nums):
        visited.add(node)
        nums.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs(graph, visited, neighbor, nums)

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = {}
        for u, v in adjacentPairs:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)

        firstNumber = None
        for u in graph.keys():
            if len(graph[u]) == 1:
                firstNumber = u
                break

        nums = []
        visited = set()
        self.dfs(graph, visited, firstNumber, nums)

        return nums
