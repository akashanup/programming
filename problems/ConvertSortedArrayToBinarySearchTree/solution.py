# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recurFn(self, nums, root):
        if nums:
            middle = len(nums) // 2
            left = nums[:middle]
            right = nums[middle + 1:]
            if left:
                root.left = TreeNode(left[len(left) // 2])
                self.recurFn(left, root.left)
            if right:
                root.right = TreeNode(right[len(right) // 2])
                self.recurFn(right, root.right)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
            Since nums is sorted so it can be assumed as the inorder traversal of BST
            Since we have to make a heigt balanced tree so the mid of nums would be the root of the tree and,
            1. root.left would be the mid of nums[:mid]
            2. root.right would be the mid of nums[mid+1:]

            Now extrapolate the above logic.
        '''
        middle = len(nums) // 2
        root = TreeNode(nums[middle])
        return self.recurFn(nums, root) if middle else root
