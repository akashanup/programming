import unittest


class Solution:
    def isGraphBipartite(self, nodes, edges):
        graph = {}
        colors = {}
        for i in range(1, nodes+1):
            graph[i] = []
            colors[i] = None
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        for i in range(1, nodes+1):
            if colors[i] is None:
                colors[i] = 1
                queue = [i]
                while queue:
                    currentNode = queue.pop(0)
                    for node in graph[currentNode]:
                        if colors[node] is None:
                            colors[node] = 1 - colors[currentNode]
                            queue.append(node)
                        elif colors[node] == colors[currentNode]:
                            return False
        return True


class Test(unittest.TestCase):
    def testIsGraphBipartite1(self):
        actual = Solution().isGraphBipartite(4, [[1, 2], [4, 1], [2, 3], [3, 1]])
        expected = 0
        self.assertEqual(actual, expected)

    def testIsGraphBipartite2(self):
        actual = Solution().isGraphBipartite(5, [[5, 2], [4, 2], [3, 4], [1, 4]])
        expected = 1
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
