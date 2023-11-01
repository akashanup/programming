"""

Intuition
If we would have to take extra space to solve this question, then it would be very easy. We would just take a hashmap and store the count of each node's value and based on that we could return the modes.
Since we have to solve it in constant time, so we have to think something out of the box with whatever information is given.
We know that we have a BST but here duplicate values could be present.
We also know that INORDER traversal of BST is always in non-decreasing order.
We can use this BST property to confirm that at any point in the traversal if a node's value is less than it's root's value then we can guarantee that the current node's value won't appear again and hence we can calculate the modes till that node in the traversal.

Approach:
Initialize an empty list as modes to store all the modes.
Initialize the modesCount and prevNodeValCount as 0 to store the maximumCount so far and the count of the previous node value.
Whenever, prevNodeValCount > modesCount then we can say that we have a new mode.
Whenever, prevNodeValCount == modesCount then we can say that we have a new mode with the same count/weight.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    modes = []
    modesCount = 0
    prevNodeVal = None
    prevNodeValCount = 0

    def dfs(self, root):
        if root:
            self.dfs(root.left)

            if root.val == self.prevNodeVal:
                self.prevNodeValCount += 1
            else:
                self.prevNodeValCount = 1

            if self.prevNodeValCount == self.modesCount:
                self.modes.append(root.val)
            elif self.prevNodeValCount > self.modesCount:
                self.modes = [root.val]
                self.modesCount = self.prevNodeValCount

            self.prevNodeVal = root.val

            self.dfs(root.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.modes
