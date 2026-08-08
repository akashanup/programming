"""
# Intuition

Since we cannot swap the values of the nodes, we need to swap the actual node links.

For every pair of nodes:
- Let the first node be `head`
- Let the second node be `head.next`

After swapping:
- The second node becomes the new head of the pair.
- The first node should point to the result of recursively swapping the remaining list.

The recursion naturally handles the rest of the list while the current call focuses only on swapping the first two nodes.

# Approach

1. Handle the base case:
   - If the list is empty or contains only one node, return it.
2. Store the start of the remaining list:
   - `nextToAdjacentNode = head.next.next`
3. Let `adjacentNode = head.next`.
4. Swap the current pair:
   - `adjacentNode.next = head`
5. Recursively swap the remaining nodes and connect them:
   - `head.next = self.swapPairs(nextToAdjacentNode)`
6. Return `adjacentNode` because it becomes the new head of the swapped pair.

# Complexity

- Time complexity:
  - O(n)

- Space complexity:
  - O(n)

The extra space is due to the recursion call stack.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        nextToAdjacentNode = head.next.next

        # swap nodes
        adjacentNode = head.next
        adjacentNode.next = head

        head.next = self.swapPairs(nextToAdjacentNode)

        return adjacentNode