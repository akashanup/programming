# Flip

You are given a binary string A(i.e. with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.

### Example 1
```sh
Input: s = "010"
Output: [0,0]
```

### Example 2
```sh
Input: s = "111"
Output: []
```

### Example 3
```sh
Input: s = "1101010001"
Output: [2, 8]
```

### Constraints
```sh
1 <= size of string <= 100000
```
