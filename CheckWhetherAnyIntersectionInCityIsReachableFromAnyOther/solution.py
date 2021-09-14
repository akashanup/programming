import unittest


class Solution:
    def explore(self, graph, visited, postVisitOrder, node):
        visited.append(node)
        for u in graph[node]:
            if u not in visited:
                self.explore(graph, visited, postVisitOrder, u)
        postVisitOrder.append(node)

    def numberOfSCC(self, n, edges):
        graph = {}
        # Reverse Graph
        graphPrime = {}
        visited = []
        postVisitOrder = []
        for i in range(1, n+1):
            graph[i] = []
            # Reverse Graph
            graphPrime[i] = []

        for u, v in edges:
            graph[u].append(v)
            graphPrime[v].append(u)

        # Source component of reverse graph will be the sink component of original graph.
        for i in range(1, n+1):
            if i not in visited:
                self.explore(graphPrime, visited, postVisitOrder, i)

        visited = []
        scc = 0
        while postVisitOrder:
            node = postVisitOrder.pop()
            if node not in visited:
                scc += 1
                self.explore(graph, visited, [], node)
        return scc


class Test(unittest.TestCase):
    def testCheckForCycle1(self):
        actual = Solution().numberOfSCC(4, [[1, 2], [4, 1], [2, 3], [3, 1]])
        expected = 2
        self.assertEqual(actual, expected)

    def testCheckForCycle2(self):
        actual = Solution().numberOfSCC(5, [[2, 1], [3, 1], [3, 2], [4, 3], [4, 1], [5, 2], [5, 3]])
        expected = 5
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
