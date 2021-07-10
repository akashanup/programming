class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Solution:
    def height(self, tree):
        if tree:
            return 1 + max(self.height(tree.left), self.height(tree.right))
        return 0

    def size(self, tree):
        if tree:
            return 1 + self.size(tree.left) + self.size(tree.right)
        return 0

    # Depth First Search
    def inOrder(self, tree):
        if tree:
            self.inOrder(tree.left)
            print(tree.key, end=" ")
            self.inOrder(tree.right)
        return

    # Depth First Search
    def preOrder(self, tree):
        if tree:
            print(tree.key, end=" ")
            self.preOrder(tree.left)
            self.preOrder(tree.right)
        return

    # Depth First Search
    def postOrder(self, tree):
        if tree:
            self.postOrder(tree.left)
            self.postOrder(tree.right)
            print(tree.key, end=" ")
        return

    # Breadth First Search
    def levelOrder(self, tree):
        if tree:
            queue = [tree]
            while len(queue):
                print(queue[0].key, end=" ")
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
