# Longest Common Subsequence of Three Sequences

Compute the length of a longest common subsequence of three sequences.

A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

Given three sequences 𝐴 = (𝑎 1 , 𝑎 2 , . . . , 𝑎 𝑛 ), 𝐵 = (𝑏 1 , 𝑏 2 , . . . , 𝑏 𝑚 ), and 𝐶 = (𝑐 1 , 𝑐 2 , . . . , 𝑐 𝑙 ), find the
length of their longest common subsequence, i.e., the largest non-negative integer 𝑝 such that there
exist indices 1 ≤ 𝑖 1 < 𝑖 2 < · · · < 𝑖 𝑝 ≤ 𝑛, 1 ≤ 𝑗 1 < 𝑗 2 < · · · < 𝑗 𝑝 ≤ 𝑚, 1 ≤ 𝑘 1 < 𝑘 2 < · · · < 𝑘 𝑝 ≤ 𝑙 such
that 𝑎 𝑖 1 = 𝑏 𝑗 1 = 𝑐 𝑘 1 , . . . , 𝑎 𝑖 𝑝 = 𝑏 𝑗 𝑝 = 𝑐 𝑘 𝑝

### Example 1
```sh
Input: a = [1, 2, 3], b = [2, 1, 3], c = [1, 3, 5]
Output: 2
```

### Example 2
```sh
Input: a = [8, 3, 2, 1, 7], b = [8, 2, 1, 3, 8, 10, 7], c = [6, 8, 3, 1, 4, 7]
Output: 3
