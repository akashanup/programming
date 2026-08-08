"""
# Intuition

Instead of using recursion, we can swap adjacent nodes one pair at a time by updating pointers.

A dummy node is placed before the head to simplify edge cases, especially when swapping the first pair. For every pair:

prev -> first -> second -> next

becomes

prev -> second -> first -> next

After the swap, move `prev` to the end of the swapped pair and continue processing the rest of the list.

# Approach

1. Create a dummy node pointing to the head.
2. Use a pointer `prev` starting at the dummy node.
3. While two nodes are available:
   - Let `first = prev.next`.
   - Let `second = first.next`.
   - Update pointers to swap the pair.
   - Move `prev` to `first` (which is now the second node in the swapped pair).
4. Return `dummy.next` as the new head of the list.

# Complexity

- Time complexity:
  - O(n)

- Space complexity:
  - O(1)

Only a few pointers are used regardless of the input size.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # swap nodes
            first.next = second.next
            second.next = first
            prev.next = second

            # move to next pair
            prev = first

        return dummy.next