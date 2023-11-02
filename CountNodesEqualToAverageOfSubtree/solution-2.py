# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getSize(self, root, lookup):
        if not root:
            return 0
        lookup[root] = 1 + self.getSize(root.left, lookup) + self.getSize(root.right, lookup)
        return lookup[root]

    def getSum(self, root, lookup):
        if not root:
            return 0
        lookup[root] = root.val + self.getSum(root.left, lookup) + self.getSum(root.right, lookup)
        return lookup[root]

    def countNodes(self, root, nodeSizes, nodeSums):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return int(root.val == int(nodeSums[root] / nodeSizes[root])) + self.countNodes(root.left, nodeSizes,
                                                                                        nodeSums) + self.countNodes(
            root.right, nodeSizes, nodeSums)

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        nodeSizes = {}
        nodeSums = {}
        self.getSize(root, nodeSizes)
        self.getSum(root, nodeSums)
        return self.countNodes(root, nodeSizes, nodeSums)