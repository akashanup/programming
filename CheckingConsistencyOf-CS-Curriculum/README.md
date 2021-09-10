# Checking Consistency of CS Curriculum

A Computer Science curriculum specifies the prerequisites for each course as a list of courses that should be
taken before taking this course. You would like to perform a consistency check of the curriculum, that is,
to check that there are no cyclic dependencies. For this, you construct the following directed graph: vertices
correspond to courses, there is a directed edge (𝑢, 𝑣) is the course 𝑢 should be taken before the course 𝑣.
Then, it is enough to check whether the resulting graph contains a cycle.

**Task:** Check whether a given directed graph with 𝑛 vertices and 𝑚 edges contains a cycle.

**Input:** Format. A graph is given in the standard format.

**Output:** Output 1 if the graph contains a cycle and 0 otherwise.

### Example 1
```sh
Input:  44
        12
        41
        23
        31
Output: 1
Explanation: This graph contains a cycle: 3 -> 1 -> 2 -> 3.
```

### Example 2
```sh
Input:  57
        12
        23
        13
        34
        14
        25
        35
Output: 0
Explanation: There is no cycle in this graph. This can be seen, for example, by noting that all edges in this graph go from a vertex with a smaller number to a vertex with a larger number.
```

### Constraints
```sh
1 <= 𝑛 <= 10^3
0 <= 𝑚 <= 10^3.
```

