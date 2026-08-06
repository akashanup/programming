# Computing the Minimum Number of Flight Segments

You would like to compute the minimum number of flight segments to get from one city to another one. For
this, you construct the following undirected graph: vertices represent cities, there is an edge between two
vertices whenever there is a flight between the corresponding two cities. Then, it suffices to find a shortest
path from one of the given cities to the other one.

**Task:** Given an undirected graph with 𝑛 vertices and 𝑚 edges and two vertices 𝑢 and 𝑣, compute the length
of a shortest path between 𝑢 and 𝑣 (that is, the minimum number of edges in a path from 𝑢 to 𝑣).

**Input:** A graph is given in the standard format. The next line contains two vertices 𝑢 and 𝑣.

**Output:** Output the minimum number of edges in a path from 𝑢 to 𝑣, or −1 if there is no path.

### Example 1
```sh
Input:  44
        12
        41
        23
        31
        24
Output: 2
Explanation: There is a unique shortest path between vertices 2 and 4 in this graph: 2 −> 1 −> 4.
```

### Example 2
```sh
Input:  54
        52
        13
        34
        14
        35
Output: -1
Explanation: There is no path between vertices 3 and 5 in this graph.
```

### Constraints
```sh
2 <= 𝑛 <= 10^5, 
0 <= 𝑚 <= 10^5, 
𝑢 != 𝑣, 
1 <= 𝑢, 𝑣 <= 𝑛.
```

