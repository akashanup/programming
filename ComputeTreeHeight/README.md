# Compute tree height

You are given a description of a rooted tree. Your task is to compute and output its height. Recall
that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a
leaf to the root.

- Input Format. The first line contains the number of nodes 𝑛. The second line contains 𝑛 integer numbers
from −1 to 𝑛 − 1 — parents of nodes. If the 𝑖-th one of them (0 ≤ 𝑖 ≤ 𝑛 − 1) is −1, node 𝑖 is the root,
otherwise it’s 0-based index of the parent of 𝑖-th node. It is guaranteed that there is exactly one root.
It is guaranteed that the input represents a tree.

- Output Format. Output the height of the tree.

### Example 1
```sh
Input: n = 5, parent = [4, -1, 4, 1, 1]
Output: 3
Explanation: The input means that there are 5 nodes with numbers from 0 to 4, node 0 is a child of node 4, node 1
is the root, node 2 is a child of node 4, node 3 is a child of node 1 and node 4 is a child of node 1. To
see this, let us write numbers of nodes from 0 to 4 in one line and the numbers given in the input in
the second line underneath:
0 1234
4 -1 4 1 1
Now we can see that the node number 1 is the root, because −1 corresponds to it in the second line.
Also, we know that the nodes number 3 and number 4 are children of the root node 1. Also, we know
that the nodes number 0 and number 2 are children of the node 4.
The height of this tree is 3, because the number of vertices on the path from root 1 to leaf 2 is 3.
```

### Example 2
```sh
Input: n = 5, parent = [-1, 0, 4, 0, 3]
Output: 4
Explanation: The input means that there are 5 nodes with numbers from 0 to 4, node 0 is the root, node 1 is a child
of node 0, node 2 is a child of node 4, node 3 is a child of node 0 and node 4 is a child of node 3. The
height of this tree is 4, because the number of nodes on the path from root 0 to leaf 2 is 4.
```

### Constraints
```sh
1 <= 𝑛 <= 10^5 .
```
