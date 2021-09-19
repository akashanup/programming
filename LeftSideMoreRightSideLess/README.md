# Left Side More Right Side Less

We have an array, we have to find the elements before which all elements are less than it, and after which all are greater than it. Finally, return the index of the elements, if there is no such element, then return -1: Time complexity O(n) and Space Complexity O(n)

### Example 1
```sh
Input: nums = [5, 1, 4, 3, 6, 8, 10, 7, 9]  
Output: [4]
Explanation: All elements on the left of arr[4] are smaller than it
and all elements on right are greater.
```
### Example 2
```sh
Input: nums = [5, 1, 4, 3, 6, 8, 10, 11, 9]  
Output: [4, 5]
Explanation: All elements on the left of arr[4] and arr[5] are smaller than it
and all elements on right are greater.
```
