"""
# Intuition

The intersection is determined by **node reference**, not by node value. If we traverse both lists with two pointers and switch each pointer to the head of the other list after reaching the end, both pointers will travel the same total distance (`lenA + lenB`).

If the lists intersect, the pointers will eventually meet at the intersection node. If they do not intersect, both pointers will reach `None` at the same time.

# Approach

1. Initialize two pointers `a` and `b` at `headA` and `headB`.
2. Traverse both lists simultaneously.
3. When pointer `a` reaches the end of list A, redirect it to `headB`.
4. When pointer `b` reaches the end of list B, redirect it to `headA`.
5. Continue until `a == b`.
6. Return the meeting node, which will either be:
   - The intersection node, or
   - `None` if no intersection exists.

This works because each pointer traverses both lists exactly once, eliminating any difference in path lengths.

# Complexity

- Time complexity:
  - `O(m + n)`

- Space complexity:
  - `O(1)`
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:B

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
```