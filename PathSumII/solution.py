# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, targetSum, paths):
        if root:
            '''
                If the current node is a leaf node then evaluate the sum of nodes from to leaf with targetSum.
                If it is equal the push the leaf node to the current path(i.e, paths[-1]) and also push the path of its parent's (i.e, paths[-1][:-1]) to calculate for other child sub tree.
            '''
            if root.left is None and root.right is None:
                if sum(paths[-1], root.val) == targetSum:
                    paths[-1].append(root.val)
                    # Go to parent
                    paths.append(paths[-1][:-1])
            elif root.left or root.right:
                paths[-1].append(root.val)
                if root.left:
                    self.dfs(root.left, targetSum, paths)
                if root.right:
                    self.dfs(root.right, targetSum, paths)
                '''
                    Go back to the parent if all the child nodes have been evaluated.
                '''
                paths[-1].pop()
        return

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = [[]]
        self.dfs(root, targetSum, paths)
        '''
            If the path of rightmost leaf from root doesn't equal to targetSum then paths will have a blank list at its last position.
            Pop that.
        '''
        if len(paths[-1]) == 0:
            paths.pop()
        return paths
