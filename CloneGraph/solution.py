# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def dfs(self, node, copy, copiedNodes):
        for neighbour in node.neighbors:
            if neighbour.val in copiedNodes:
                copy.neighbors.append(copiedNodes[neighbour.val])
            else:
                copiedNodes[neighbour.val] = Node(neighbour.val)
                copy.neighbors.append(copiedNodes[neighbour.val])
                self.dfs(neighbour, copy.neighbors[-1], copiedNodes)

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        copiedNodes = {node.val: Node(node.val)}
        copy = copiedNodes[node.val]
        self.dfs(node, copy, copiedNodes)
        return copy


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
print(Solution().cloneGraph(node1))
