# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, level, ans):
        if not root:
            return
        if level > ans[1]:
            ans[0], ans[1] = root.val, level
        elif level == ans[1]:
            ans[0] += root.val
        self.dfs(root.left, level + 1, ans)
        self.dfs(root.right, level + 1, ans)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = [0, 0]
        self.dfs(root, 0, ans)
        print(ans)
        return ans[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(7)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(8)

print(Solution().deepestLeavesSum(root))
