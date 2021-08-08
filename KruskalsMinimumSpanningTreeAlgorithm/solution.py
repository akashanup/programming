class DisjointSet:
    def __init__(self, vertices):
        self.parent = [i for i in range(vertices)]
        self.rank = [0] * vertices

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        parent1 = self.find(vertex1)
        parent2 = self.find(vertex2)
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent2] > self.rank[parent1]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += 1


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def addEdge(self, vertex1, vertex2, weight):
        self.graph.append([vertex1, vertex2, weight])

    def KruskalMST(self):
        self.graph.sort(key=lambda x: x[2])
        minimumCostSpanningTree = 0
        # Initialize disjoint sets
        disjointSet = DisjointSet(self.vertices)
        i = 0
        edge = 0
        # Minimum spanning tree has (V-1) edges.
        while edge < self.vertices - 1:
            vertex1, vertex2, weight = self.graph[i]
            i += 1
            parent1 = disjointSet.find(vertex1)
            parent2 = disjointSet.find(vertex2)
            if parent1 != parent2:
                minimumCostSpanningTree += weight
                disjointSet.union(vertex1, vertex2)
                edge += 1
        return minimumCostSpanningTree


'''
Time Complexity: O(ElogE) or O(ElogV). 
Sorting of edges takes O(ELogE) time. 
After sorting, we iterate through all edges and apply the find-union algorithm. 
The find and union operations can take at most O(LogV) time. S
o overall complexity is O(ELogE + ELogV) time. T
he value of E can be at most O(V2), so O(LogV) is O(LogE) the same. 
Therefore, the overall time complexity is O(ElogE) or O(ElogV)
graph = Graph(4)
graph.addEdge(0, 1, 10)
graph.addEdge(0, 2, 6)
graph.addEdge(0, 3, 5)
graph.addEdge(1, 3, 15)
graph.addEdge(2, 3, 4)
print(graph.KruskalMST())
'''

