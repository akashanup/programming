# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        # Traverse till the node from where we need to reverse the linked list.
        linkedList = None
        for i in range(left - 1):
            if linkedList:
                linkedList = linkedList.next
            else:
                linkedList = head

        # Assign the starting node to a temporary linked list from which the linked list will be reversed
        if linkedList:
            tempLinkedList = linkedList.next
        else:
            tempLinkedList = None
        reversedLinkedList = None

        # Reverse the linked list from left to right location and assign it to temporary linked list
        for i in range(left, right + 1):
            if reversedLinkedList:
                newNode = ListNode(tempLinkedList.val)
                newNode.next = reversedLinkedList
                reversedLinkedList = newNode
            else:
                if tempLinkedList is None:
                    tempLinkedList = head
                reversedLinkedList = ListNode(tempLinkedList.val)
            tempLinkedList = tempLinkedList.next

        # Append the initial linked list with the reversed linked list
        if linkedList:
            linkedList.next = reversedLinkedList
        else:
            head = linkedList = reversedLinkedList

        # Append the inital linked list with the remaining nodes after the reversal
        while linkedList:
            if linkedList.next:
                linkedList = linkedList.next
            else:
                linkedList.next = tempLinkedList
                break
        return head
