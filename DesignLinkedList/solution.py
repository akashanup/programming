"""
# Intuition

To efficiently handle insertions and deletions at the beginning of the list, we use a **sentinel (dummy) node**. The sentinel node simplifies edge cases because every operation can be treated as inserting or deleting after some previous node.

We also maintain the current **size** of the linked list. This allows us to validate indices in O(1) time and ensures that operations such as `get`, `addAtIndex`, and `deleteAtIndex` follow the problem constraints correctly.

# Approach

- Use a singly linked list with a **sentinel node** whose `next` pointer always points to the first real node.
- Maintain a variable `size` to track the number of nodes in the list.
- For `get(index)`:
  - Return `-1` if the index is invalid.
  - Traverse to the target node and return its value.
- For `addAtHead(val)`:
  - Insert at index `0`.
- For `addAtTail(val)`:
  - Insert at index `size`.
- For `addAtIndex(index, val)`:
  - If `index > size`, do nothing.
  - Traverse to the node just before the insertion position.
  - Insert the new node by updating pointers.
- For `deleteAtIndex(index)`:
  - If the index is invalid, do nothing.
  - Traverse to the node just before the deletion position.
  - Remove the target node by skipping it.

# Complexity

- Time complexity:
  - `get`: **O(n)**
  - `addAtHead`: **O(1)**
  - `addAtTail`: **O(n)**
  - `addAtIndex`: **O(n)**
  - `deleteAtIndex`: **O(n)**

- Space complexity:
  - **O(1)**
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.sentinel = ListNode()   # sentinel node
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.sentinel.next

        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0

        if index > self.size:
            return

        prev = self.sentinel

        for _ in range(index):
            prev = prev.next

        prev.next = ListNode(val, prev.next)

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.sentinel

        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index, val)
# obj.deleteAtIndex(index)