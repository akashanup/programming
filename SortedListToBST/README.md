# Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

[![linkedlist](linked.jpg)]()

### Example1
```sh
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
```

### Example2
```sh
Input: head = []
Output: []
```

### Example3
```sh
Input: head = [0]
Output: [0]
```

### Example4
```sh
Input: head = [1,3]
Output: [3,1]
```

### Constraints
```sh
The number of nodes in head is in the range [0, 2 * 104].
-10^5 <= Node.val <= 10^5
```
