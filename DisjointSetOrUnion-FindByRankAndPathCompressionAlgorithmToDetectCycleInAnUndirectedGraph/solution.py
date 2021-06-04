class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}

    def addEdge(self, v1, v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
        else:
            self.graph[v1] = [v2]

    def findParent(self, subsets, node):
        if subsets[node].parent == node:
            return subsets[node].parent
        else:
            return self.findParent(subsets, subsets[node].parent)

    @staticmethod
    def union(subsets, v1, v2):
        if subsets[v1].rank > subsets[v2].rank:
            subsets[v2].parent = v1
        elif subsets[v2].rank > subsets[v1].rank:
            subsets[v1].parent = v2
        else:
            subsets[v2].parent = v1
            subsets[v1].rank += 1

    def initializeSubset(self):
        return {i: Subset(i, 0) for i in self.vertices}

    def isCyclic(self):
        subsets = self.initializeSubset()
        # Iterate through all edges of graph,
        # find sets of both vertices of every
        # edge, if sets are same, then there
        # is cycle in graph.
        for i in self.graph:
            x = self.findParent(subsets, i)
            for j in self.graph[i]:
                y = self.findParent(subsets, j)
                if x == y:
                    return True
                else:
                    self.union(subsets, x, y)
        return False


graph = Graph([1, 2, 3, 4, 5])
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(3, 4)
graph.addEdge(3, 5)
graph.addEdge(4, 5)
print(graph.isCyclic())
