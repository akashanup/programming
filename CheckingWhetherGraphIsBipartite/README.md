# Checking whether a Graph is Bipartite

An undirected graph is called bipartite if its vertices can be split into two parts such that each edge of the
graph joins to vertices from different parts. Bipartite graphs arise naturally in applications where a graph
is used to model connections between objects of two different types (say, boys and girls; or students and
dormitories).

An alternative definition is the following: a graph is bipartite if its vertices can be colored with two colors
(say, black and white) such that the endpoints of each edge have different colors.

**Task:** Given an undirected graph with 𝑛 vertices and 𝑚 edges, check whether it is bipartite.

**Input:** A graph is given in the standard format.

**Output:** Output 1 if the graph is bipartite and 0 otherwise.

### Example 1
```sh
Input:  44
        12
        41
        23
        31
Output: 0
Explanation: This graph is not bipartite. To see this assume that the vertex 1 is colored white. Then the vertices 2
and 3 should be colored black since the graph contains the edges {1, 2} and {1, 3}. But then the edge
{2, 3} has both endpoints of the same color.
```

### Example 2
```sh
Input:  54
        52
        42
        34
        14
Output: 1
Explanation: This graph is bipartite: assign the vertices 4 and 5 the white color, assign all the remaining vertices
the black color.
```

### Constraints
```sh
1 <= 𝑛 <= 10^4
0 <= 𝑚 <= 10^4.
```

