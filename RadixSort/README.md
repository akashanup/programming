# Radix Sort

The idea of Radix Sort is to do digit by digit sort starting from the least significant digit to most significant digit. Radix sort uses counting sort as a subroutine to sort.

If we have log2n bits for every digit, the running time of Radix appears to be better than Quick Sort for a wide range of input numbers.

Radix Sort takes O(d*(n+b)) time where b is the base for representing numbers, for example, for the decimal system, b is 10.

### Example 1
```sh
Input: arr = [992, 17, 536, 992, 516, 745, 246, 418, 242, 245, 676, 131, 850, 895, 410, 957, 109, 638, 551, 498]
Output: [17, 109, 131, 242, 245, 246, 410, 418, 498, 516, 536, 551, 638, 676, 745, 850, 895, 957, 992, 992]
```
