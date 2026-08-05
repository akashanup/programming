"""
# Intuition

A child list should be inserted immediately after its parent node and before the parent's original next node. This naturally suggests a Depth First Search (DFS) approach.

For every node:
1. Flatten its child list recursively.
2. Splice the flattened child list between the current node and its original next node.
3. Return the tail of the flattened segment so that the parent call can reconnect the remaining list efficiently.

Returning both the head and tail of the flattened list allows us to connect sublists in O(1) time without repeatedly traversing to find the tail.

# Approach

- Use a recursive DFS helper `flattenDfs(head)` that returns `(head, tail)` of the flattened list starting at `head`.
- Traverse the current level node by node.
- Store `curr.next` before modifying any pointers.
- If a child exists:
  - Recursively flatten the child list.
  - Set `curr.child = None`.
  - Insert the flattened child list after `curr`.
  - Connect the child list's tail to the original next node.
- Keep track of the latest tail encountered.
- Continue processing using the original `nextNode`.
- The main `flatten()` function simply invokes DFS and returns the original head.

# Complexity

- Time complexity:
  
  $$O(n)$$

  Each node is visited exactly once.

- Space complexity:
  
  $$O(d)$$

  Where `d` is the maximum depth of nesting due to the recursion stack. In the worst case, this can be $$O(n)$$.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flattenDfs(self, head):
        curr = head
        tail = head

        while curr:
            nextNode = curr.next
            tail = curr

            if curr.child is not None:
                childHead, childTail = self.flattenDfs(curr.child)

                curr.child = None

                # Insert child list after curr
                curr.next = childHead
                childHead.prev = curr

                # Connect child tail to original next node
                childTail.next = nextNode
                if nextNode:
                    nextNode.prev = childTail

                tail = childTail

            curr = nextNode

        return head, tail

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        self.flattenDfs(head)
        return head