#  Maximum Unsorted Subarray

Given an array A of non-negative integers of size N. Find the minimum sub-array Al, Al+1 ,..., Ar such that if we sort(in ascending order) that sub-array, then the whole array should get sorted.
If A is already sorted, output -1.

### Example 1
```sh
Input: A = [1, 3, 2, 4, 5]
Output: [1, 2]
Explanation: If we sort the sub-array A1, A2, then the whole array A gets sorted.
```

### Example 2
```sh
Input: A = [1, 2, 3, 4, 5]
Output: [-1]
Explanation: A is already sorted.
```

### Constraints
```sh
1 <= N <= 1000000
1 <= A[i] <= 1000000
```
