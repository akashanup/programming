# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        verticalNodes = {}
        queue = [[0, 0, root]]
        while queue:
            currentX = queue[0][0]
            currentY = queue[0][1]
            currentNode = queue[0][2]
            if currentX in verticalNodes:
                currentNodesAtX = verticalNodes[currentX]
                if currentY in currentNodesAtX:
                    currentNodesAtY = currentNodesAtX[currentY]
                    currentNodesAtY.append(currentNode.val)
                    currentNodesAtX[currentY] = currentNodesAtY
                else:
                    currentNodesAtX[currentY] = [currentNode.val]
                verticalNodes[currentX] = currentNodesAtX
            else:
                verticalNodes[currentX] = {currentY: [currentNode.val]}
            queue.pop(0)
            if currentNode.left is not None:
                queue.append([currentX - 1, currentY + 1, currentNode.left])
            if currentNode.right is not None:
                queue.append([currentX + 1, currentY + 1, currentNode.right])
        verticalTraversing = []
        for x in sorted(verticalNodes.keys()):
            currentNodesAtX = []
            for y in sorted(verticalNodes[x].keys()):
                for node in sorted(verticalNodes[x][y]):
                    currentNodesAtX.append(node)
            verticalTraversing.append(currentNodesAtX)
        return verticalTraversing
