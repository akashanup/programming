# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
            Using the property of BST that if the values of the given nodes are greater then root then it must be present in right subtree or else if the values are less then root then it must be present in left subtree.
			If any of the value is equal to the root then that root must be the LCA of the given two nodes.
        '''
        while True:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


node = TreeNode(6)
node.left = TreeNode(2)
node.right = TreeNode(8)
node.left.left = TreeNode(0)
node.left.right = TreeNode(4)
node.right.left = TreeNode(7)
node.right.right = TreeNode(9)
node.left.right.left = TreeNode(3)
node.left.right.right = TreeNode(5)
print(Solution().lowestCommonAncestor(node, node.left, node.left.right))
