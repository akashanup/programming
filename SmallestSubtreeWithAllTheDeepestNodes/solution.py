# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # Find deepest nodes
        queue = deque([root])
        deepestNodes = []
        while queue:
            deepestNodes = queue.copy()
            for i in range(len(deepestNodes)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        """
        Now we need to find LCA of first and last deepestNodes as all the intermediate deepestNodes would definitely
        have the same LCA.
        Edge case: If there is only one deepest node then return its parent
        """
        if len(deepestNodes) > 1:
            return self.__findLCA(root, deepestNodes[0], deepestNodes[-1])
        else:
            return self.__findParent(root, deepestNodes[0])

    def __findLCA(self, root, node1, node2):
        path1 = []
        self.__findPath(root, node1, path1)
        path2 = []
        self.__findPath(root, node2, path2)
        i = 0
        minPathLen = min(len(path1), len(path2))
        while i < minPathLen:
            if path1[i].val != path2[i].val:
                break
            i += 1
        return path1[i - 1]

    def __findPath(self, root, node, path):
        if not root:
            return False
        path.append(root)
        if root.val == node.val:
            return True
        if self.__findPath(root.left, node, path):
            return True
        if self.__findPath(root.right, node, path):
            return True
        path.pop()
        return False

    def __findParent(self, root, node):
        if not root:
            return None
        if root.val == node.val:
            return root
        parent = self.__findParent(root.left, node)
        if not parent:
            parent = self.__findParent(root.right, node)
        return parent