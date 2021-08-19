# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, root, lookup):
        if root:
            '''
                For each node, store the sum of values of nodes present in its subtree.
            '''
            if not root.left and not root.right:
                lookup[root] = root.val
            else:
                lookup[root] = root.val + (self.recur(root.left, lookup) if root.left else 0) + (self.recur(root.right, lookup) if root.right else 0)
            return lookup[root]

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        lookup = {}
        self.recur(root, lookup)
        answer = 0
        for l in lookup:
            '''
                Find the maximum product of a node with its subtree and rest of tree.
            '''
            answer = max(answer, (lookup[root] - lookup[l]) * lookup[l])
        return answer % ((10**9) + 7)
