# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum = -sys.maxsize
        self.__dfs(root)
        return self.maxPathSum

    def __dfs(self, root):
        if root:
            leftVal = 0
            if root.left:
                self.__dfs(root.left)
                leftVal = max(root.left.val)

            rightVal = 0
            if root.right:
                self.__dfs(root.right)
                rightVal = max(root.right.val)

            rootVal = root.val
            """
            Keep updated the value of a node with (its current value, its current value + max value of its left subtree, its current value + max value of its right subtree)
            Note: We aren't storing (its current value +  max value of its left subtree + max value of its right subtree) becaue this value could not be used by its parent as two nodes in the path must be adjacent. So we could either take root's value itself OR root's value and it's either of the children, BUT not both.
            """
            root.val = (rootVal, rootVal+leftVal, rootVal+rightVal)
            """
            However, while calculating the maxSum we could use both its subtrees as it would be a valid path.
            """
            self.maxPathSum = max(self.maxPathSum, max(root.val), rootVal+leftVal+rightVal)