# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head, reversedLinkedList=None):
        if not head:
            return reversedLinkedList
        next = head.next
        head.next = reversedLinkedList
        return self.reverseList(next, head)

    '''
        if not head:
            return head
        reversedLinkedList = None
        while head:
            if not reversedLinkedList:
                reversedLinkedList = head
                head = head.next
                reversedLinkedList.next = None
            else:
                temp = head
                head = head.next
                temp.next = reversedLinkedList
                reversedLinkedList = temp
        return reversedLinkedList
    '''
