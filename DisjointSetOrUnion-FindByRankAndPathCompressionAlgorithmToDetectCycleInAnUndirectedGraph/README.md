# Disjoint Set (Union By Rank and Path Compression Algorithm) | (Detect Cycle in an Undirected Graph)

A disjoint-set data structure is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.

The application disjoint-set data structure is to check whether a given graph contains a cycle or not.
Union By Rank and Path Compression Algorithm can be used to check whether an undirected graph contains cycle or not.

The operations of [naive](https://github.com/akashanup/programming/tree/main/DisjointSetOrUnion-FindAlgorithmToDetectCycleInAnUndirectedGraph) method for this can be optimized to O(Log n) in worst case.

The idea is to always attach smaller depth tree under the root of the deeper tree. This technique is called union by rank. The term rank is preferred instead of height because if path compression technique is used, then rank is not always equal to height. Also, size (in place of height) of trees can also be used as rank. Using size as rank also yields worst case time complexity as O(Logn)

The second optimization to naive method is Path Compression. The idea is to flatten the tree when find() is called. When find() is called for an element x, root of the tree is returned. The find() operation traverses up from x to find root. The idea of path compression is to make the found root as parent of x so that we don’t have to traverse all intermediate nodes again. If x is root of a subtree, then path (to root) from all nodes under x also compresses.
