# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertListToBST(self, arr):
        if not arr:
            return None
        middle = (len(arr))//2
        root = TreeNode(arr[middle])
        root.left = self.convertListToBST(arr[:middle])
        root.right = self.convertListToBST(arr[middle+1:])
        return root
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head and head.val is not None:
            #Convert LinkedList to List
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            #Convert List to height balanced BST
            return self.convertListToBST(arr)
        else:
            return self.convertListToBST([])