# Longest Common Subsequence of Two Sequences

Compute the length of a longest common subsequence of two sequences.

A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

Given two sequences 𝐴 = (𝑎 1 , 𝑎 2 , . . . , 𝑎 𝑛 ) and 𝐵 = (𝑏 1 , 𝑏 2 , . . . , 𝑏 𝑚 ), find the length of their longest
common subsequence, i.e., the largest non-negative integer 𝑝 such that there exist indices 1 ≤ 𝑖 1 <
𝑖 2 < · · · < 𝑖 𝑝 ≤ 𝑛 and 1 ≤ 𝑗 1 < 𝑗 2 < · · · < 𝑗 𝑝 ≤ 𝑚, such that 𝑎 𝑖 1 = 𝑏 𝑗 1 , . . . , 𝑎 𝑖 𝑝 = 𝑏 𝑗 𝑝 .

### Example 1
```sh
Input: a = 275, b = 25
Output: 2
```

### Example 2
```sh
Input: a = 7, b = 1234
Output: 0
```
### Example 1
```sh
Input: a = 2783, b = 5287
Output: 2
```
