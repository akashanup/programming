# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

    def createBST(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        rootIndex = self.binarySearch(inorder, preorder[0])
        root.left = self.createBST(preorder[1:rootIndex+1], inorder[:rootIndex])
        root.right = self.createBST(preorder[rootIndex+1:], inorder[rootIndex+1:])
        return root


    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        return self.createBST(preorder, inorder)

