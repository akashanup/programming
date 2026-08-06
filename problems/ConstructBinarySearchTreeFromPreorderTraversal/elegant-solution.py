# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def createBST(self, preorder, maxVal):
        if not preorder or preorder[-1] > maxVal:
            return None
        root = TreeNode(preorder.pop())
        root.left = self.createBST(preorder, root.val)
        root.right = self.createBST(preorder, maxVal)
        return root


    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
            Since it is a BST therefore, the value of root would always be greater than its left child.
            By the above fact, we can divide the preorder array into three half-
            1. Root -> 0th index would be the root
            2. Left Subtree -> From 1st index of preorder till the index of last element which is less root value.
            3. Right Subtree -> From the first index of element which is greater than root till end
            We can use the above logic and keep slicing the array by recursion to get the left and right subtree for each node. If at any point the value becomes greater than the root value we can return None as that can't be the part of left subtree and then it will go in right subtree.
        """
        return self.createBST(preorder[::-1], sys.maxsize)

