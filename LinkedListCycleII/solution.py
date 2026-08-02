"""
# Intuition

We use **Floyd's Tortoise and Hare Algorithm** to solve the problem in **O(1) space**.

The solution has two phases:

1. **Detect the cycle**
   - Move `slow` by 1 step and `fast` by 2 steps.
   - If they meet, a cycle exists.
   - If `fast` reaches `None`, there is no cycle.

2. **Find the cycle entry**
   - Let:
     - `L` = distance from `head` to the cycle start
     - `x` = distance from the cycle start to the meeting point
     - `C` = length of the cycle

   At the meeting point:

   ```
   2(L + x) = L + x + kC
   ```

   Simplifying:

   ```
   L + x = kC
   ```

   Therefore:

   ```
   L = kC - x
   ```

   This means the distance from the meeting point to the cycle start is equal to the distance from `head` to the cycle start (modulo the cycle length).

   So, if one pointer starts from `head` and the other starts from the meeting point, and both move one step at a time, they will meet at the cycle entry.

---

# Approach

1. Initialize two pointers `slow` and `fast` at `head`.
2. Move:
   - `slow` one step at a time.
   - `fast` two steps at a time.
3. If they never meet, return `None`.
4. Once they meet:
   - Reset `slow` to `head`.
   - Keep `fast` at the meeting point.
5. Move both pointers one step at a time.
6. The node where they meet is the start of the cycle.

### What if we reset `fast` instead of `slow`?

After detecting the cycle, this is equally valid:

```python
fast = head

while slow is not fast:
    slow = slow.next
    fast = fast.next

return slow
```

or

```python
slow = head

while slow is not fast:
    slow = slow.next
    fast = fast.next

return slow
```

Both pointers move with the same speed, so they will meet at the cycle entry. The choice of which pointer to reset is purely stylistic.

---

# Complexity

- Time complexity:

$$O(n)$$

- Space complexity:

$$O(1)$$

---
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # Phase 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break
        else:
            return None

        # Phase 2: Find cycle entry
        slow = head

        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow