# Interleave The First Half Of The Queue With The Second Half

You have been given a queue of integers. 
You need to rearrange the elements of the queue by interleaving the elements of the first half of the queue with the second half.

NOTE: 
1. The given queue will always be of even length.
2. You can only use a stack as an auxiliary space.

### Example 1
```sh
Input: Q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Output: Q = [10, 60, 20, 70, 30, 80, 40, 90, 50, 100]
Explanation: 2 = 1 + 1, 1 × 1 = 1.
```

### Constraints
```sh
2 <= len(Q) <= 10^3
0 <= Q[i] <= 10^4
```
