# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        if not root:
            return values

        queue = deque([(root, 0)])
        while queue:
            root, index = queue.popleft()
            if index == len(values):
                values.append(root.val)
            else:
                values[-1] = max(root.val, values[-1])
            if root.left:
                queue.append((root.left, index+1))
            if root.right:
                queue.append((root.right, index+1))

        return values
