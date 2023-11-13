import heapq
from typing import List

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = {i: {} for i in range(n)}
        for edge in edges:
            from_node, to_node, cost = edge
            self.graph[from_node][to_node] = cost

    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.graph[from_node][to_node] = cost

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 not in self.graph or node2 not in self.graph:
            return -1

        heap = [(0, node1)]
        visited = set()

        while heap:
            current_cost, current_node = heapq.heappop(heap)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == node2:
                return current_cost

            for neighbor, cost in self.graph[current_node].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (current_cost + cost, neighbor))

        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)