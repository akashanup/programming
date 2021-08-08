class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}
        self.parent = {}
        self.rank = {}

    def addEdge(self, v1, v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
        else:
            self.graph[v1] = [v2]

    def findParent(self, i):
        if i == self.parent[i]:
            return i
        return self.findParent(self.parent[i])

    def union(self, i, j):
        x = self.findParent(i)
        y = self.findParent(j)
        # If both the vertices belong to same subset then union can't be performed.
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[y] > self.rank[x]:
            self.parent[x] = y
        else:
            # Either do this.
            self.parent[y] = x
            self.rank[x] += 1
            # Or do this.
            # self.parent[x] = y
            # self.rank[y] += 1

    def makeSet(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def isCyclic(self):
        # Initialize sets
        [self.makeSet(i) for i in self.vertices]

        # Iterate through all edges of graph,
        # find sets of both vertices of every edge,
        # If sets are same, then there is cycle in graph.
        for i in self.graph:
            x = self.findParent(i)
            for j in self.graph[i]:
                y = self.findParent(j)
                if x == y:
                    return True
                else:
                    self.union(x, y)
        return False


graph = Graph([1, 2, 3, 4, 5])
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(3, 4)
graph.addEdge(3, 5)
graph.addEdge(4, 5)
print(graph.isCyclic())
