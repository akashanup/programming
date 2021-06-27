class LinkedList:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:
    def printLinkedList(self, linkedList):
        linkedListElements = []
        while linkedList:
            linkedListElements.append(linkedList.val)
            linkedList = linkedList.next
        return linkedListElements

    def insertionSort(self, head):
        if head:
            sortedList = LinkedList(head.val)
            head = head.next
            while head:
                if sortedList.val >= head.val:
                    node = LinkedList(head.val)
                    node.next = sortedList
                    sortedList = node
                else:
                    current = sortedList
                    next = current.next
                    while next:
                        if next.val >= head.val:
                            break
                        current = next
                        next = current.next
                    node = LinkedList(head.val)
                    current.next = node
                    node.next = next
                head = head.next
        else:
            return None
        return sortedList


ll = LinkedList(5)
ll.next = LinkedList(8)
ll.next.next = LinkedList(0)
ll.next.next.next = LinkedList(9)
ll.next.next.next.next = LinkedList(21)
ll.next.next.next.next.next = LinkedList(0)
ll.next.next.next.next.next.next = LinkedList(3)
ll.next.next.next.next.next.next.next = LinkedList(-1)
ll.next.next.next.next.next.next.next.next = LinkedList(3)
ll.next.next.next.next.next.next.next.next.next = LinkedList(4)
ll.next.next.next.next.next.next.next.next.next.next = LinkedList(12)
ll.next.next.next.next.next.next.next.next.next.next.next = LinkedList(-2)
print(Solution().printLinkedList(ll))
print(Solution().printLinkedList(Solution().insertionSort(ll)))
