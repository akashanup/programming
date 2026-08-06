class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}

    def addEdge(self, v1, v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
        else:
            self.graph[v1] = [v2]

    def findParent(self, parent, i):
        if parent[i] == -1:
            return i
        else:
            return self.findParent(parent, parent[i])

    @staticmethod
    def union(parent, x, y):
        parent[x] = y

    def initializeParent(self):
        return {i: -1 for i in self.vertices}

    def isCyclic(self):
        parent = self.initializeParent()
        # Iterate through all edges of graph,
        # find sets of both vertices of every
        # edge, if sets are same, then there
        # is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x, y = self.findParent(parent, i), self.findParent(parent, j)
                if x == y:
                    return True
                else:
                    self.union(parent, x, y)
        return False


graph = Graph([1, 2, 3, 4, 5])
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(3, 4)
graph.addEdge(3, 5)
graph.addEdge(4, 5)
print(graph.isCyclic())
