# Longest Common Subsequence of Two Sequences

Compute the length of a longest common subsequence of two sequences.

A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

Given two sequences ๐ด = (๐ 1 , ๐ 2 , . . . , ๐ ๐ ) and ๐ต = (๐ 1 , ๐ 2 , . . . , ๐ ๐ ), find the length of their longest
common subsequence, i.e., the largest non-negative integer ๐ such that there exist indices 1 โค ๐ 1 <
๐ 2 < ยท ยท ยท < ๐ ๐ โค ๐ and 1 โค ๐ 1 < ๐ 2 < ยท ยท ยท < ๐ ๐ โค ๐, such that ๐ ๐ 1 = ๐ ๐ 1 , . . . , ๐ ๐ ๐ = ๐ ๐ ๐ .

### Example 1
```sh
Input: a = [2, 7, 5], b = [2, 5]
Output: 2
```

### Example 2
```sh
Input: a = [7], b = [1, 2, 3, 4]
Output: 0
```
### Example 3
```sh
Input: a = [2, 7, 8, 3], b = [5, 2, 8, 7]
Output: 2
```
