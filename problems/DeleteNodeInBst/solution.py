"""
Logic:
Traverse the tree till the key is found. While traversing keep a pointer parent to point the parent of current node. This pointer will be used when deletion will happen.
If key is not found then simply return the root.
Else, Find whether there is a right subtree of the target node.
    If yes then goto the leftmost leaf of right subtree and attach the root of left subtree of target node to it. This is done to maintain the BST.
    Else, directly attach the root of left subtree of target node to the parent.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        tempRoot = root
        parent = None
        while root and root.val != key:
            parent = root
            if root.val < key:
                root = root.right
            else:
                root = root.left

        # If key is not found.
        if root is None:
            return tempRoot

        if root.right:
            child = root.right
            while child.left:
                child = child.left
            child.left = root.left
            if parent:
                if parent.left and parent.left.val == root.val:
                    parent.left = root.right
                else:
                    parent.right = root.right
            else:
                tempRoot = root.right
        else:
            if parent:
                if parent.left and parent.left.val == root.val:
                    parent.left = root.left
                else:
                    parent.right = root.left
            else:
                tempRoot = root.left
            root.left = root.right = None
        return tempRoot
