# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
			# If the value of a node is None then it means we are visiting this node again. Hence a cycle is present
            if head.val == None:
                return True
			# Modify the value of each visited node to None.
            head.val = None
            head = head.next
            
        return False