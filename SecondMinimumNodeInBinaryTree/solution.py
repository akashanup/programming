# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys


class Solution:
    def checkNextMinimum(self, root, minimum):
        if not root:
            return sys.maxsize
        if root.val == minimum:
            root.val = sys.maxsize
        return min(root.val, self.checkNextMinimum(root.left, minimum), self.checkNextMinimum(root.right, minimum))
        
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        secondMin = self.checkNextMinimum(root, root.val)
        return secondMin if secondMin != sys.maxsize else -1

