"""
### Intuition
Perform DFS and keep the track for maximum difference.

### Approach
Since we have to find the absolute maximum difference between an ancestor and a node, so we need to keep track of
maximum and minimum values encountered for each node in DFS to get the absolute maximum difference.

### Complexity
Time complexity:
O(h) where h is the height of the tree.

### Space complexity:
O(n) where n in the number of nodes.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return max(self.__dfs(root.left, root.val, root.val), self.__dfs(root.right, root.val, root.val))

    def __dfs(self, root, maxVal, minVal):
        if root:
            rootDiff = max(abs(maxVal - root.val), abs(root.val - minVal))
            leftDiff = self.__dfs(root.left, max(root.val, maxVal), min(root.val, minVal))
            rightDiff = self.__dfs(root.right, max(root.val, maxVal), min(root.val, minVal))
            return max(rootDiff, leftDiff, rightDiff)
        return -sys.maxsize