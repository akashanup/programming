# Subarrays with distinct elements

Given an array, the task is to calculate the sum of lengths of contiguous subarrays having all elements distinct.

### Example 1
```sh
Input :  arr[] = {1, 2, 3}
Output : 10
    {1, 2, 3} is a subarray of length 3 with 
    distinct elements. Total length of length
    three = 3.
    {1, 2}, {2, 3} are 2 subarray of length 2 
    with distinct elements. Total length of 
    lengths two = 2 + 2 = 4
    {1}, {2}, {3} are 3 subarrays of length 1
    with distinct element. Total lengths of 
    length one = 1 + 1 + 1 = 3
    Sum of lengths = 3 + 4 + 3 = 10
```

### Example 2
```sh
Input :  arr[] = {1, 2, 1}
Output : 7
```

### Example 3
```sh
Input :  arr[] = {1, 2, 3, 4}
Output : 20
```
