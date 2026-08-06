# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        stack = [root]
        visited = set()
        while stack:
            root = stack[-1]
            if root:
                if root not in visited:
                    visited.add(root)
                    stack.append(root.left)
                elif root.right and root.right not in visited:
                    stack.append(root.right)
                else:
                    root = stack.pop()
                    postorder.append(root.val)
            else:
                stack.pop()

        return postorder
