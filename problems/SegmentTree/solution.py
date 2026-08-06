class Node:

    def __init__(self, startInterval, endInterval, data=0, left=None, right=None):
        self.startInterval = startInterval
        self.endInterval = endInterval
        self.data = data
        self.left = left
        self.right = right


class SegmentTree:
    root: Node

    def __init__(self, arr: list):
        self.root = self.__constructTree(arr, 0, len(arr)-1)

    def __constructTree(self, arr: list, start: int, end: int) -> Node:
        if start == end:
            leaf: Node = Node(start, end, arr[start])
            return leaf
        node: Node = Node(start, end)
        mid: int = (start + end) // 2
        node.left = self.__constructTree(arr, start, mid)
        node.right = self.__constructTree(arr, mid+1, end)
        node.data = node.left.data + node.right.data
        return node

    def display(self):
        self.__display(self.root)

    def __display(self, node: Node) -> None:
        s: str = ""
        if node.left:
            s = (s + "Interval=[" + str(node.left.startInterval) + "-" + str(node.left.endInterval) + "] and data: "
                 + str(node.left.data) + " =>")
        else:
            s = s + "No left child =>"

        s = (s + " Interval=[" + str(node.startInterval) + "-" + str(node.endInterval) + "] and data: " + str(node.data)
             + " <=")

        if node.right:
            s = (s + " Interval=[" + str(node.right.startInterval) + "-" + str(node.right.endInterval) + "] and data: "
                 + str(node.right.data))
        else:
            s = s + " No right child"

        print(s)
        if node.left:
            self.__display(node.left)
        if node.right:
            self.__display(node.right)

    def query(self, start: int, end: int) -> int:
        return self.__query(self.root, start, end)

    def __query(self, node: Node, start: int, end: int) -> int:
        if node.startInterval >= start and node.endInterval <= end:
            return node.data
        elif node.startInterval > end or node.endInterval < start:
            return 0
        else:
            return self.__query(node.left, start, end) + self.__query(node.right, start, end)

    def update(self, index: int, value: int) -> None:
        self.root.data = self.__update(self.root, index, value)

    def __update(self, node: Node, index: int, value: int) -> int:
        if node.startInterval <= index <= node.endInterval:
            if index == node.startInterval and index == node.endInterval:
                node.data = value
                return node.data
            else:
                leftAns: int = self.__update(node.left, index, value)
                rightAns: int = self.__update(node.right, index, value)
                node.data = leftAns + rightAns
                return node.data
        return node.data


class Solution:
    arr = [3, 8, 6, 7, -2, -8, 4, 9]
    segmentTree: SegmentTree = SegmentTree(arr)
    segmentTree.display()
    print(segmentTree.query(1, 6))
