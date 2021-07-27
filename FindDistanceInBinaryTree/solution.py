"""
Assume p or q or both are not present in list.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findPath(self, root, node, path):
        if not root:
            return False
        path.append(root.val)
        if root.val == node:
            return True
        if (root.left and self.findPath(root.left, node, path)) or (root.right and self.findPath(root.right, node, path)):
            return True
        path.pop()
        return False

    def lowestCommonAncestor(self, root, p, q):
        pathP = []
        pathQ = []
        if (not self.findPath(root, p.val, pathP)) or (not self.findPath(root, q.val, pathQ)):
            return - 1
        i = 0
        while i < len(pathP) and i < len(pathQ):
            if pathP[i] != pathQ[i]:
                # Lowest common ancestors would be present at i - 1 index
                i -= 1
                break
            i += 1
        # No. of edges would be No. of nodes - 1
        return len(pathP[i:]) - 1 + len(pathQ[i:]) - 1


node = TreeNode(3)
node.left = TreeNode(5)
node.right = TreeNode(1)
node.left.left = TreeNode(6)
node.left.right = TreeNode(2)
node.right.left = TreeNode(0)
node.right.right = TreeNode(8)
node.left.right.left = TreeNode(7)
node.left.right.right = TreeNode(4)
print(Solution().lowestCommonAncestor(node, node.left, node.right.left))
# print(Solution().lowestCommonAncestor(node, node.right.left, node.left.right.left))
