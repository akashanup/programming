import unittest


class Solution:
    def minimumNumberOfFlights(self, nodes, edges, u, v):
        graph = {}
        visited = {}
        for i in range(1, nodes+1):
            graph[i] = []
            visited[i] = False
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        queue = [[0, u]]
        while queue:
            currentLevel, currentNode = queue.pop(0)
            if currentNode == v:
                return currentLevel
            for node in graph[currentNode]:
                if not visited[node]:
                    visited[node] = True
                    queue.append([currentLevel+1, node])
        return -1


class Test(unittest.TestCase):
    def testMinimumNumberOfFlights1(self):
        actual = Solution().minimumNumberOfFlights(4, [[1, 2], [4, 1], [2, 3], [3, 1]], 2, 4)
        expected = 2
        self.assertEqual(actual, expected)

    def testMinimumNumberOfFlights2(self):
        actual = Solution().minimumNumberOfFlights(5, [[5, 2], [1, 3], [3, 4], [1, 4]], 3, 5)
        expected = -1
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
