"""
# Intuition

Since nodes can be removed from anywhere in the list, including the head, using a sentinel (dummy) node simplifies the pointer manipulation. The sentinel node points to the original head and allows us to handle head deletions the same way as any other node deletion.

We maintain two pointers:
- `curr` to traverse the list.
- `prev` to track the last valid node that remains in the list.

When `curr.val == val`, we remove the current node by connecting `prev.next` directly to the next node. Otherwise, we move `prev` forward.

# Approach

1. Create a sentinel node whose `next` points to `head`.
2. Initialize:
   - `prev = sentinel`
   - `curr = head`
3. Traverse the list:
   - Store `curr.next` before any modification.
   - If `curr.val == val`, remove the node by updating `prev.next`.
   - Otherwise, move `prev` to `curr`.
4. Move `curr` to the next node.
5. Return `sentinel.next` as the new head.

# Complexity

- Time complexity:
  - $$O(n)$$
  - Each node is visited exactly once.

- Space complexity:
  - $$O(1)$$
  - Only a few pointers are used regardless of input size.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        prev = sentinel
        curr = head

        while curr:
            nextNode = curr.next

            if curr.val == val:
                prev.next = nextNode
                curr.next = None
            else:
                prev = curr

            curr = nextNode

        return sentinel.next