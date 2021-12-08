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
        if not root.left and not root.right:
            value = root.val
            root.val = 0
            return value, tiltSum
        leftSubTreeTilt, tiltSum = self.recur(root.left, tiltSum)
        rightSubTreeTilt, tiltSum = self.recur(root.right, tiltSum)
        value = root.val + rightSubTreeTilt + leftSubTreeTilt
        tilt = abs(rightSubTreeTilt - leftSubTreeTilt)
        root.val = tilt
        return value, tiltSum+tilt

    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.recur(root, 0)[1]

