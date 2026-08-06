class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class TreeHeight:
    def __init__(self, n, parent):
        self.n = n
        self.parent = parent

    def constructTree(self):
        nodes = []
        for i in range(self.n):
            nodes.append(Node(i))

        tree = None
        for i in range(self.n):
            if self.parent[i] == -1:
                tree = nodes[i]
            else:
                if nodes[self.parent[i]].left:
                    nodes[self.parent[i]].right = nodes[i]
                else:
                    nodes[self.parent[i]].left = nodes[i]
        return tree

    def computeHeight(self):
        tree = self.constructTree()
        if tree:
            queue = [[1, tree]]
            node = None
            while len(queue):
                node = queue.pop(0)
                if node[1].left:
                    queue.append([node[0] + 1, node[1].left])
                if node[1].right:
                    queue.append([node[0] + 1, node[1].right])
            return node[0]
        return 0
