from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getPath(self, root, node, path):
        if root == node:
            return True
        if not root:
            return False
        path.append(-1)
        if self.getPath(root.left, node, path):
            return True
        path.pop()
        path.append(1)
        if self.getPath(root.right, node, path):
            return True
        path.pop()
        return False

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        path = deque([])
        # path will have values in either 1 or -1.
        # 1 means, target is present in right subtree
        # -1 means target is present in left subtree
        self.getPath(original, target, path)
        while path:
            direction = path.popleft()
            if direction == 1:
                cloned = cloned.right
            else:
                cloned = cloned.left
        return cloned
