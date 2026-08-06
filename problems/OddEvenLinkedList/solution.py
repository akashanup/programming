"""
# Intuition

The list needs to be reordered based on node positions, not node values.

The first node is considered odd-indexed, the second node is even-indexed, and so on. So the idea is to split the original list into two separate chains:

- One chain for odd-indexed nodes.
- One chain for even-indexed nodes.

While traversing the original list, we attach each node to the appropriate chain. After the traversal is complete, we connect the end of the odd chain to the beginning of the even chain.

Using sentinel nodes makes the logic easier to write and reason about because we do not need separate handling for the first odd or even node beyond initialization.

# Approach

1. Create two sentinel nodes:
   - `sentinelOdd` for the odd-indexed nodes.
   - `sentinelEven` for the even-indexed nodes.

2. Use two pointers:
   - `currOdd` to track the tail of the odd list.
   - `currEven` to track the tail of the even list.

3. Traverse the original list using `curr`.

4. Keep a boolean flag `isOddIndex`:
   - If `True`, attach the current node to the odd list.
   - If `False`, attach the current node to the even list.

5. Before modifying links, save the next node:

   ```python
   nextNode = curr.next
   ```

6. Detach the current node from the original list:

   ```python
   curr.next = None
   ```

   This keeps both newly formed lists clean and avoids accidental cycles.

7. After traversal, connect the odd list with the even list:

   ```python
   currOdd.next = sentinelEven.next
   ```

8. Return the head of the odd list:

   ```python
   sentinelOdd.next
   ```

# Complexity

- Time complexity:
  - $$O(n)$$
  - Each node is visited exactly once.

- Space complexity:
  - $$O(1)$$
  - Only a constant number of pointers and two sentinel nodes are used.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        isOddIndex = True
        sentinelOdd = ListNode()
        currOdd = None
        sentinelEven = ListNode()
        currEven = None
        curr = head
        
        while curr:
            nextNode = curr.next
            if isOddIndex:
                if currOdd:
                    currOdd.next = curr
                else:
                    sentinelOdd.next = curr
                currOdd = curr
            else:
                if currEven:
                    currEven.next = curr
                else:
                    sentinelEven.next = curr
                currEven = curr
            curr.next = None
            curr = nextNode
            isOddIndex = not isOddIndex
            
        if currOdd:
            currOdd.next = sentinelEven.next
            sentinelEven.next = None
            
        return sentinelOdd.next