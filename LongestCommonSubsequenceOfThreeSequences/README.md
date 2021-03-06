# Longest Common Subsequence of Three Sequences

Compute the length of a longest common subsequence of three sequences.

A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

Given three sequences ๐ด = (๐ 1 , ๐ 2 , . . . , ๐ ๐ ), ๐ต = (๐ 1 , ๐ 2 , . . . , ๐ ๐ ), and ๐ถ = (๐ 1 , ๐ 2 , . . . , ๐ ๐ ), find the
length of their longest common subsequence, i.e., the largest non-negative integer ๐ such that there
exist indices 1 โค ๐ 1 < ๐ 2 < ยท ยท ยท < ๐ ๐ โค ๐, 1 โค ๐ 1 < ๐ 2 < ยท ยท ยท < ๐ ๐ โค ๐, 1 โค ๐ 1 < ๐ 2 < ยท ยท ยท < ๐ ๐ โค ๐ such
that ๐ ๐ 1 = ๐ ๐ 1 = ๐ ๐ 1 , . . . , ๐ ๐ ๐ = ๐ ๐ ๐ = ๐ ๐ ๐

### Example 1
```sh
Input: a = [1, 2, 3], b = [2, 1, 3], c = [1, 3, 5]
Output: 2
```

### Example 2
```sh
Input: a = [8, 3, 2, 1, 7], b = [8, 2, 1, 3, 8, 10, 7], c = [6, 8, 3, 1, 4, 7]
Output: 3
