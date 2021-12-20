# House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

[![rob1-tree](rob1-tree.jpg)]()
### Example 1
```sh
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
```

[![rob2-tree](rob2-tree.jpg)]()
### Example 2
```sh
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
```

### Example 3
```sh
Input: nums = [1,2,3]
Output: 3
```

### Constraints
```sh
The number of nodes in the tree is in the range [1, 10^4].
0 <= Node.val <= 10^4
```
