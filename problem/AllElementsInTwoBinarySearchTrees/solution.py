# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root):
        return ((self.inorder(root.left)) + [root.val] + (self.inorder(root.right))) if root else []
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        inorder1 = self.inorder(root1)
        inorder2 = self.inorder(root2)
        result = []
        i1, i2 = 0, 0
        while True:
            if i1 < len(inorder1) and i2 < len(inorder2):
                if inorder1[i1] <= inorder2[i2]:
                    result.append(inorder1[i1])
                    i1 += 1
                else:
                    result.append(inorder2[i2])
                    i2 += 1
            elif i1 < len(inorder1):
                result.append(inorder1[i1])
                i1 += 1
            elif i2 < len(inorder2):
                result.append(inorder2[i2])
                i2 += 1
            else:
                break
        return result
