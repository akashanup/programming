"""
# Intuition

A right rotation by `k` positions moves the last `k` nodes to the front of the list.

Instead of moving nodes one by one, we can first determine the length of the list and connect the tail back to the head to form a circular linked list. Once the list is circular, the problem reduces to finding the new tail. The node immediately after the new tail becomes the new head. Finally, we break the circle to restore the linked list structure.

# Approach

1. Handle edge cases where the list is empty, contains only one node, or `k = 0`.
2. Traverse the list once to find:
   - The length of the list.
   - The tail node.
3. Reduce unnecessary rotations using:
   ```python
   k %= length
   ```
4. If `k == 0`, return the original list.
5. Connect the tail to the head to create a circular linked list.
6. Find the new tail by moving `length - k - 1` steps from the head.
7. The node after the new tail becomes the new head.
8. Break the circular link and return the new head.

# Complexity

- Time complexity:
  $$O(n)$$

- Space complexity:
  $$O(1)$$
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations
        k %= length
        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find the new tailw_tail = length - k - 1
        new_tail = head

        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # New head
        new_head = new_tail.next

        # Break the cycle
        new_tail.next = None

        return new_head