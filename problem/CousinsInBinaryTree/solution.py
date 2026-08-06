# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, x, y, depth, parent, found):
        if not root:
            return
        if root.val == x or root.val == y:
            found.append((depth, parent.val if parent else -1))
        if len(found) == 2:
            return
        self.dfs(root.left, x, y, depth+1, root, found)
        self.dfs(root.right, x, y, depth+1, root, found)
        return 
    
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # No node can be the cousin of root so straight away return False
        if root.val == x or root.val == y:
            return False
        
        """
            We will do depth first search for both x and y and once they are found, we will simply verify their depth and parent. If they have same depth and different parent, return True Else False.
            We will store the depth and parent of x and y in found array.
        """
        found = []
        self.dfs(root, x, y, 0, None, found)
        return found[0][0] == found[1][0] and found[0][1] != found[1][1]
    
