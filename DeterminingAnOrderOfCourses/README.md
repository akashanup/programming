# Determining an Order of Courses

Now, when you are sure that there are no cyclic dependencies in the given CS curriculum, you would like to
find an order of all courses that is consistent with all dependencies. For this, you find a topological ordering
of the corresponding directed graph.

**Task:** Compute a topological ordering of a given directed acyclic graph (DAG) with 𝑛 vertices and 𝑚 edges.

**Input Format:** A graph is given in the standard format.

**Output Format:** Output any topological ordering of its vertices. (Many DAGs have more than just one
topological ordering. You may output any of them.)

### Example 1
```sh
Input:  43
        12
        41
        31

Output: 4 3 1 2
```

### Example 2
```sh
Input:  41
        31
Output: 2 3 1 4
```

### Example 3
```sh
Input:  57
        21
        32
        31
        43
        41
        52
        53
Output: 5 4 3 2 1
```

### Constraints
```sh
1 <= 𝑛 <= 10^5, 
0 <= 𝑚 <= 10^5. 
The given graph is guaranteed to be acyclic.
```
