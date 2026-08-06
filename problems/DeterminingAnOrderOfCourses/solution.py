import unittest


class Solution:
    def explore(self, graph, visited, postVisit, node):
        visited[node] = True
        for u in graph[node]:
            if not visited[u]:
                self.explore(graph, visited, postVisit, u)
        postVisit.append(node)

    def topologicalOrder(self, n, edges):
        graph = {}
        visited = {}
        postVisit = []
        for i in range(1, n+1):
            graph[i] = []
            visited[i] = False
        for u, v in edges:
            graph[u].append(v)
        for i in range(1, n+1):
            if not visited[i]:
                self.explore(graph, visited, postVisit, i)
        postVisit.reverse()
        return postVisit


class Test(unittest.TestCase):
    def testTopologicalOrder1(self):
        actual = Solution().topologicalOrder(5, [[2, 1], [3, 2], [3, 1], [4, 3], [4, 1], [5, 2], [5, 3]])
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(actual, expected)

    def testTopologicalOrder2(self):
        actual = Solution().topologicalOrder(4, [[1, 2], [4, 1], [3, 1]])
        expected = [4, 3, 1, 2]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
