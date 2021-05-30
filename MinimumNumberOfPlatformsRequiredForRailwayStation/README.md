# Minimum Number of Platforms Required for a Railway Station

Given the arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits. 
We are given two arrays that represent the arrival and departure times of trains that stop.

### Example 1
```sh
Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00} 
dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00} 
Output: 3 
Explanation: There are at-most three trains at a time (time between 11:00 to 11:20)
```

### Example 2
```sh
Input: arr[] = {9:00, 9:40} 
dep[] = {9:10, 12:00} 
Output: 1 
Explanation: Only one platform is needed. 
```
