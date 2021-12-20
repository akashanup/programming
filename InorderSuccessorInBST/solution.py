# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findLeftMostLeaf(self, node):
        while node.left:
            node = node.left
        return node

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        currNode = root
        parent = {root: None}
        while currNode and currNode.val != p.val:
            if currNode.val < p.val:
                if currNode.right:
                    parent[currNode.right] = currNode
                currNode = currNode.right
            else:
                if currNode.left:
                    parent[currNode.left] = currNode
                currNode = currNode.left
        if currNode:
            if currNode.right:
                return self.findLeftMostLeaf(currNode.right)
            elif currNode in parent:
                while parent[currNode]:
                    currNode = parent[currNode]
                    if currNode.val > p.val:
                        return currNode
        return None
