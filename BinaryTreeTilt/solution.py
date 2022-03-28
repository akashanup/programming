# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, root, tiltSum):
        if not root:
            return 0, tiltSum
        leftSubTreeSum, tiltSum = self.recur(root.left, tiltSum)
        rightSubTreeSum, tiltSum = self.recur(root.right, tiltSum)
        value = root.val + leftSubTreeSum + rightSubTreeSum
        tilt = abs(rightSubTreeSum - leftSubTreeSum)
        return value, tiltSum+tilt

    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.recur(root, 0)[1]

