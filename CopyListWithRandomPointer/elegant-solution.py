"""
# Intuition

Instead of using a hash map to maintain the mapping between original and copied nodes, we can temporarily interleave the copied nodes within the original linked list itself.

By placing every copied node immediately after its corresponding original node:

```
A -> B -> C

becomes

A -> A' -> B -> B' -> C -> C'
```

This arrangement allows us to determine the random pointer of every copied node in **O(1)** time.

If the random pointer of an original node points to `R`, then the random pointer of its copied node should point to `R'`, which is simply `R.next`.

After assigning the random pointers, we detach the copied nodes to form the deep-copied linked list and restore the original list.

---

# Approach

### Step 1: Insert copied nodes after original nodes

Traverse the original linked list and insert a copied node immediately after each original node.

```
A -> B -> C

becomes

A -> A' -> B -> B' -> C -> C'
```

### Step 2: Assign random pointers

Since every copied node is placed right after its original node:

- `original.random = R`
- `copied.random = R.next`

because `R.next` is the copied version of `R`.

### Step 3: Separate the two lists

Restore the original list by reconnecting original nodes while simultaneously extracting the copied nodes into a new list.

After separation:

```
Original:
A -> B -> C

Copied:
A' -> B' -> C'
```

Return the head of the copied list.

---

# Complexity

- Time complexity:

$$O(n)$$

We traverse the list three times:

1. Insert copied nodes.
2. Assign random pointers.
3. Separate the two lists.

Overall complexity remains **O(n)**.

<br>

- Space complexity:

$$O(1)$$

No extra data structures such as a hash map are used. The copied nodes themselves are part of the required output and therefore do not contribute to auxiliary space.

---
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Add the copied node without random pointer just after its corresponding original node.
        node = head
        while node:
            copiedNode = Node(node.val, node.next)
            node.next = copiedNode
            node = copiedNode.next
        
        """
        Update the random pointer of each copied node.

        If:
            original.random = R

        Then:
            copied.random = R.next

        because every copied node is placed immediately after
        its corresponding original node.
        """
        node = head
        while node:
            copiedNode = node.next
            if node.random:
                copiedNode.random = node.random.next
            node = copiedNode.next
        
        # Separate the copied list from the original list.
        copiedHead = head.next
        node = head

        while node:
            copiedNode = node.next
            node.next = copiedNode.next
            node = node.next

            if copiedNode.next:
                copiedNode.next = copiedNode.next.next

        return copiedHead