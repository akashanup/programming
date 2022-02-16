# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        tempHead = None
        prevNode = None
        while head and head.next:
            # Swap the current and next node.
            current = head
            next = head.next
            current.next = next.next
            next.next = current
            # If current node is the first node then update the head.
            if not tempHead:
                tempHead = next
            else:
                # Update the next pointer of previous node to the current node after swapping.
                prevNode.next = next
            # Keep track of previous node would be used in next swap
            prevNode = current
            # Move the pointer to next the starting node of next pair.
            head = current.next
        
        return tempHead
            
