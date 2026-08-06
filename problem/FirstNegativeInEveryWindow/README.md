# First Negative In Every Window

Your task is to find the first negative element in every window (contiguous subarray) of length 'K'. 
If there is no negative element in a window, then print 0 for that window.

### Example 1
```sh
Input: nums = [5, -3, 2, 3, -4] and k = 2.
Output: [-3, -3, 0, -4]
Explanation:
We have four windows of length 2 in nums
[5, -3] having -3 as first negative element.
[-3, 2] having -3 as first negative element.
[2, 3] having no negative element
[2, -4] having -4 as first negative element.
```

### Constraints
```sh
1 <= ARR.length <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
```
