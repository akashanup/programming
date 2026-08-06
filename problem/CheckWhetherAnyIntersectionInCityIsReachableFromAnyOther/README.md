# Checking Whether Any Intersection in a City is Reachable from Any Other

The police department of a city has made all streets one-way. You would like
to check whether it is still possible to drive legally from any intersection to
any other intersection. For this, you construct a directed graph: vertices are
intersections, there is an edge (𝑢, 𝑣) whenever there is a (one-way) street from
𝑢 to 𝑣 in the city. Then, it suffices to check whether all the vertices in the
graph lie in the same strongly connected component.

**Task:** Compute the number of strongly connected components(SCC) of a given directed graph with 𝑛 vertices and
𝑚 edges.

**Input:** A graph is given in the standard format.

**Output:** Output the number of strongly connected components.

### Example 1
```sh
Input:  44
        12
        41
        23
        31
Output: 2
Explanation: This graph has two strongly connected components: {1, 3, 2}, {4}.
```

### Example 2
```sh
Input:  57
        21
        32
        31
        43
        41
        52
        53
Output: 5
Explanation: This graph has five strongly connected components: {1}, {2}, {3}, {4}, {5}.
```

### Constraints
```sh
1 <= 𝑛 <= 10^4
0 <= 𝑚 <= 10^4.
```

