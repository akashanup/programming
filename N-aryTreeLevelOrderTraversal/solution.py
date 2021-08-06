# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node'):
        queue = deque([[0, root]])
        levelOrderTraversal = {}
        while queue:
            currentNode = queue.popleft()
            if currentNode[0] in levelOrderTraversal:
                levelOrderTraversal[currentNode[0]].append(currentNode[1].val)
            else:
                levelOrderTraversal[currentNode[0]] = [currentNode[1].val]
            if currentNode[1].children:
                for child in currentNode[1].children:
                    queue.append([currentNode[0] + 1, child])
        return list(levelOrderTraversal.values())


root = Node(1)
child11 = Node(3)
child12 = Node(2)
child13 = Node(4)
child21 = Node(5)
child22 = Node(6)
child11.children = [child21, child22]
root.children = [child11, child12, child13]
print(Solution().levelOrder(root))

