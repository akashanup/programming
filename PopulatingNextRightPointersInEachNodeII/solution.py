"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node', parent=None) -> 'Node':
        if not root:
            return None
        levelOrder = {}
        queue = deque([[root, 0]])
        while queue:
            node, level = queue.popleft()
            if level in levelOrder:
                levelOrder[level].append(node)
            else:
                levelOrder[level] = [node]
            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])

        for level, nodes in levelOrder.items():
            for i in range(len(nodes)):
                if i != len(nodes) - 1:
                    nodes[i].next = nodes[i + 1]

        return root
