class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        tempHead = self.head
        while tempHead:
            if i == index:
                return tempHead.val
            tempHead = tempHead.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head:
            node.next = self.head
        self.head = node  

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head:
            tempHead = self.head
            while tempHead.next:
                tempHead = tempHead.next
            tempHead.next = node
        else:
            self.head = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            i = 0
            tempHead = self.head
            while tempHead:
                if i == index-1:
                    nextNode = tempHead.next
                    newNode = Node(val, nextNode)
                    tempHead.next = newNode
                    break
                i += 1
                tempHead = tempHead.next

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head:
            self.head = self.head.next
        else:
            i = 0
            tempHead = self.head
            while tempHead:
                if i == index-1:
                    if tempHead.next: 
                        tempHead.next = tempHead.next.next
                        break
                i += 1
                tempHead = tempHead.next


# Your MyLinkedList object will be instantiated and called as such:
# myLinkedList = MyLinkedList()
# myLinkedList.addAtHead(1)
# myLinkedList.addAtTail(3)
# myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
# print(myLinkedList.get(1))              # return 2
# myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
# print(myLinkedList.get(1))