"""
Intuition:
    Instead of trying to cover every node from the top down, let's try to cover it from the bottom up.
    Consider placing a camera with the deepest nodes first, and working our way up the tree.
    If a node has its children covered and has a parent, then it is strictly better to place the camera at this node's parent.
Algorithm:
    If a node has children that are not covered by a camera, then we must place a camera here.
    Additionally, if a node has no parent and it is not covered, we must place a camera here.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        covered = {None}

        def dfs(node, parent=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if ((parent is None and node not in covered) or
                        node.left not in covered or node.right not in covered):
                    self.ans += 1
                    covered.update({node, parent, node.left, node.right})

        dfs(root)
        return self.ans
