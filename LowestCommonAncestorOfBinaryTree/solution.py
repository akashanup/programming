# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAncestorsList(self, tree, nodeVal):
        ancestors = []
        while nodeVal in tree:
            ancestors.append(tree[nodeVal])
            nodeVal = tree[nodeVal]
        return ancestors

    def getTreeDict(self, root, tree):
        if root:
            if root.left:
                left = root.left
                tree[left.val] = root.val
                self.getTreeDict(left, tree)
            if root.right:
                right = root.right
                tree[right.val] = root.val
                self.getTreeDict(right, tree)

    def lowestCommonAncestor(self, root, p, q):
        if p.val == root.val or q.val == root.val:
            return root
        tree = {}
        # Get a dictionary of all the nodes as indexes and their parent as respective values
        self.getTreeDict(root, tree)
        # Get a list of all the ancestors of a node
        pAncestor = self.getAncestorsList(tree, p.val)
        qAncestor = self.getAncestorsList(tree, q.val)
        if p.val in qAncestor:
            return TreeNode(p.val)
        if q.val in pAncestor:
            return TreeNode(q.val)
        for i in pAncestor:
            if i in qAncestor or i == q.val:
                return TreeNode(i)
        for i in qAncestor:
            if i in pAncestor or i == p.val:
                return TreeNode(i)


node = TreeNode(3)
node.left = TreeNode(5)
node.right = TreeNode(1)
node.left.left = TreeNode(6)
node.left.right = TreeNode(2)
node.right.left = TreeNode(0)
node.right.right = TreeNode(8)
node.left.right.left = TreeNode(7)
node.left.right.right = TreeNode(4)
# print(Solution().lowestCommonAncestor(node, node.left, node.right).val)
print(Solution().lowestCommonAncestor(node, node.right.left, node.left.right.left).val)
