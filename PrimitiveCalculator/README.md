# Primitive Calculator

You are given a primitive calculator that can perform the following three operations with
the current number x: multiply x by 2, multiply x by 3, or add 1 to x. Your goal is given a
positive integer n, find the minimum number of operations needed to obtain the number n
starting from the number 1.

Given an integer n, compute the minimum number of operations needed to obtain the number n
starting from the number 1.

- Input Format. The input consists of a single integer 1 ≤ n ≤ 10 6 .
- Output Format. In the first line, output the minimum number k of operations needed to get n from 1.
In the second line output a sequence of intermediate numbers. That is, the second line should contain
positive integers a 0 , a 2 , . . . , a k−1 such that a 0 = 1, a k−1 = n and for all 0 ≤ i < k − 1, a i+1 is equal to
either a i + 1, 2a i , or 3a i . If there are many such sequences, output any one of them.

### Example 1
```sh
Input: n = 1
Output: 0
        1
```

### Example 2
```sh
Input: n = 5
Output: 3
        1 2 4 5
Explanation: Here, we first multiply 1 by 2 two times and then add 1. Another possibility is to first multiply by 3
and then add 1 two times. Hence “1 3 4 5” is also a valid output in this case.
```

### Example 3
```sh
Input: n = 96234
Output: 14
        1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
Explanation: Again, another valid output in this case is “1 3 9 10 11 33 99 297 891 2673 8019 16038 16039 48117
96234”.
```
