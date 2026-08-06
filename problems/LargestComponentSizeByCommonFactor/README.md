# Largest Component Size by Common Factor

You are given an integer array of unique positive integers nums. Consider the following graph:

- There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
- There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.

Return the size of the largest connected component in the graph.

[![ex1](ex1.png)]()
### Example 1
```sh
Input: nums = [4,6,15,35]
Output: 4
```

[![ex2](ex2.png)]()
### Example 2
```sh
Input: nums = [20,50,9,63]
Output: 2
```

[![ex3](ex3.png)]()
### Example 3
```sh
Input: nums = [2,3,6,7,4,12,21,39]
Output: 8
```

### Constraints
```sh
1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^5
All the values of nums are unique.
```
