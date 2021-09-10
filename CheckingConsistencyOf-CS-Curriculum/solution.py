import unittest


class Solution:
    def explore(self, graph, visited, lookup, node):
        visited[node] = True
        lookup[node] = True
        for u in graph[node]:
            if lookup[u]:
                return 1
            if not visited[u]:
                return self.explore(graph, visited, lookup, u)
        lookup[node] = False
        return 0

    def checkForCycle(self, n, edges):
        visited = {}
        lookup = {}
        graph = {}
        for i in range(1, n+1):
            graph[i] = []
            visited[i] = False
            lookup[i] = False
        for u, v in edges:
            graph[u].append(v)
        for i in range(1, n+1):
            if not visited[i]:
                if self.explore(graph, visited, lookup, i):
                    return 1
        return 0


class Test(unittest.TestCase):
    def testCheckForCycle1(self):
        actual = Solution().checkForCycle(4, [[1, 2], [4, 1], [2, 3], [3, 1]])
        expected = 1
        self.assertEqual(actual, expected)

    def testCheckForCycle2(self):
        actual = Solution().checkForCycle(5, [[1, 2], [1, 3], [2, 3], [3, 4], [1, 4], [2, 5], [3, 5]])
        expected = 0
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
