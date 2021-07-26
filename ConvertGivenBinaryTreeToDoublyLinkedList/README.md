# Convert a given Binary Tree to Doubly Linked List

Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. 

The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. 

The order of nodes in DLL must be the same as in Inorder for the given Binary Tree. 

The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

[![TreeToList](TreeToList.png)]()
### Example 1
```sh
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
```

### Constraints
```sh
Time Complexity: Time complexity should be O(n) where n is the number of nodes in given binary tree.
```
