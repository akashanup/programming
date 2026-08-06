# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.linkedList = None

    def createSortedListFromBST(self, root, nodes):
        if root:
            self.createSortedListFromBST(root.left, nodes)
            nodes.append(root)
            self.createSortedListFromBST(root.right, nodes)

    def createLinkedListFromBST(self, root):
        nodes = []
        self.createSortedListFromBST(root, nodes)
        lList = None
        for node in nodes:
            if lList is None:
                lList = node
                node.left = None
                node.right = None
                self.linkedList = lList
            else:
                node.left = lList
                node.right = None
                lList.right = node
                lList = lList.right

    def insert(self, val):
        lList = self.linkedList
        while lList:
            if lList.val < val:
                if lList.right:
                    lList = lList.right
                else:
                    # Insert at last position
                    node = TreeNode(val)
                    lList.right = node
                    node.left = lList
                    return
            elif lList.val > val:
                # Insert at this position
                node = TreeNode(val)
                previous = lList.left
                if previous:
                    previous.right = node
                else:
                    # Insert at first position
                    self.linkedList = node
                node.left = previous
                node.right = lList
                lList.left = node
                return
            else:
                # Duplicate value
                return

    def delete(self, val):
        lList = self.linkedList
        while lList:
            if lList.val == val:
                # Delete
                previous = lList.left
                if previous:
                    previous.right = lList.right
                    right = lList.right
                    if right:
                        right.left = previous
                    lList.left = None
                    lList.right = None
                else:
                    # Delete at first position
                    right = lList.right
                    if right:
                        right.left = None
                    self.linkedList = right
                    lList.right = None
                return
            lList = lList.right

    def printLinkedList(self):
        linkedList = self.linkedList
        while linkedList:
            print(linkedList.val, end=' ')
            linkedList = linkedList.right
        print()

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if self.linkedList is None:
            self.createLinkedListFromBST(root)
        lList = self.linkedList
        i = 1
        while i < k:
            lList = lList.right
            i += 1
        return lList.val

