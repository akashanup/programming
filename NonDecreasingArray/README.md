# Non-decreasing Array

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

### Example1

```sh
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
```
### Example2

```sh
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
```
### Example3

```sh
Input: nums = [3,4,2,3]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
```
### Example4

```sh
Input: nums = [5,7,1,8]
Output: true
Explanation: You could modify the 1 to get a non-decreasing array.
```
