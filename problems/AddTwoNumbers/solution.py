# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initially the carry is 0
        carry = 0
        # Declare a sentinel node so that we don't have to worry about the head.
        sentinel = node = ListNode()
        while l1 or l2:
            if l1 and l2:
                sumVal = carry + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sumVal = carry + l1.val
                l1 = l1.next
            else:
                sumVal = carry + l2.val
                l2 = l2.next
            # Since we have to store the unit digit only in the node and remaining must be carried forward.
            carry = sumVal // 10
            node.next = ListNode(sumVal % 10)
            node = node.next
        # If there is something left to carry forward then add nodes for each digit in carry
        while carry:
            node.next = ListNode(carry % 10)
            carry //= 10
        # return head
        return sentinel.next
