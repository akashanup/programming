# Sum of minimum and maximum elements of all subarrays of size “K”

You are given an array consisting of N integers, and an integer, K. 
Your task is to determine the total sum of the minimum element and the maximum element of all subarrays of size K.

NOTE:
- The array may contain duplicate elements.
- The array can also contain negative integers.
- The size of the array is at least 2.
- There exists at least one such subarray of size k.

### Example 1
```sh
Input: arr = [1, 2, 3, 4, 5], N = 3
Output: 18
Explanation: For the subarray starting from the 0th index and ending at the 2nd index, its minimum element is 1 and the maximum element is 3. 
  Similarly, for the next subarray starting at the 1st index and ending at the 3rd index, the minimum value is 2 and the maximum is 4. 
  And, for the last subarray, the minimum value is 3 and the maximum is 5. So, the total sum will be 1 + 3 + 2 + 4 + 3 + 5 = 18.
```

### Constraints
```sh
1 <= K <= N <= 10^5
1 <= arr[i] <= 10^9
```
