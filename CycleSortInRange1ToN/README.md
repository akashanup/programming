# Cycle Sort In Range 1 To N

Given an array arr[] of elements from 1 to N, the task is to sort the given array in O(N) time.

### Example 1
```sh
Input: arr[] = { 2, 1, 5, 4, 3} 
Output: 1 2 3 4 5 
Explanation: 
    Since arr[0] = 2 is not at correct position, then swap arr[0] with arr[arr[0] – 1] 
    Now array becomes: arr[] = {1, 2, 5, 4, 3}
    Now arr[2] = 5 is not at correct position, then swap arr[2] with arr[arr[2] – 1] 
    Now the array becomes: arr[] = {1, 2, 3, 4, 5} 
    Now the array is sorted.
```
