class Solution:
    def dfs(self, s, graph, node, visited, nodes, indices):
        visited[node] = True
        nodes.append(s[node])
        indices.append(node)
        for v in graph[node]:
            if not visited[v]:
                self.dfs(s, graph, v, visited, nodes, indices)
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        graph = [[] for _ in range(len(s))]
        
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * len(s)
        for node in range(len(s)):
            if not visited[node]:
                nodes, indices = [], []
                self.dfs(s, graph, node, visited, nodes, indices)
                nodes.sort()
                indices.sort()
                for key,index in enumerate(indices):
                    s[index] = nodes[key]
                            
        return ''.join(s)
