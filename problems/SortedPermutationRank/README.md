# Sorted Permutation Rank

Given a string A. Find the rank of the string amongst its permutations sorted lexicographically.

Assume that no characters are repeated.

Note: The answer might not fit in an integer, so return your answer % 1000003

### Example 1
```sh
Input: A = "acb"
Output: 2
Explanation: Given A = "acb".
The order permutations with letters 'a', 'c', and 'b' : 
    abc
    acb
    bac
    bca
    cab
    cba
  So, the rank of A is 2.
```

### Example 2
```sh
Input: A = "a"
Output: 1
Explanation: Given A = "a".
  Rank is clearly 1.
```

### Constraints
```sh
1 <= |A| <= 1000
```
