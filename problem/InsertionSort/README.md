# Insertion Sort

To sort an array of size n in ascending order by using Insertion sort: 
- Iterate from arr[1] to arr[n] over the array. 
- Compare the current element (key) to its predecessor. 
- If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

### Example 1
```sh
Input: arr = [5, 8, 12, 9, 21, 0, 3, -1, 3, 4, -2]
Output: [-2, -1, 0, 3, 3, 4, 5, 8, 9, 12, 21]
```
