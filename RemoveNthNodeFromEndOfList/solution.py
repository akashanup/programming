"""
# Intuition

The problem asks us to remove the `n`th node from the end of a singly linked list. Instead of first finding the length of the list and then locating the target node, we can use two pointers with a fixed gap of `n` nodes between them.

By moving the `fast` pointer `n` steps ahead of the `slow` pointer, and then advancing both pointers together, when `fast` reaches the last node, `slow` will be positioned just before the node that needs to be removed.

A sentinel (dummy) node is used before the head to elegantly handle edge cases, such as removing the first node of the list.

# Approach

1. Create a sentinel node whose `next` points to the head.
2. Initialize both `fast` and `slow` pointers at the sentinel node.
3. Move the `fast` pointer `n` steps ahead.
4. Move both `fast` and `slow` one step at a time until `fast` reaches the last node.
5. At this point, `slow.next` is the node to be removed.
6. Remove the node by updating:
   ```python
   slow.next = slow.next.next
   ```
7. Return `sentinel.next` as the new head of the modified list.

# Complexity

- Time complexity:

  $$O(n)$$

  We traverse the linked list at most once.

- Space complexity:

  $$O(1)$$

  Only a few extra pointers are used.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optionalsentinel = ListNode(next=head)
        fast = sentinel
        slow = sentinel

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both until fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # slow.next is the node to remove
        slow.next = slow.next.next

        return sentinel.next