"""
# Intuition

Instead of treating this as a linked list problem, we can view it as a graph cloning problem where each node has up to two outgoing edges: `next` and `random`.

While cloning a node, we may encounter the same node again through another path (especially via `random` pointers). To avoid creating duplicate copies and to handle cycles, we store each original node and its corresponding copied node in a hashmap.

Whenever we encounter a node:
- If it has already been copied, return the existing copy from the hashmap.
- Otherwise, create a new copy, store it in the hashmap, and recursively clone its `next` and `random` neighbors.

# Approach

1. Initialize a hashmap with `{None: None}` to naturally handle null pointers.
2. Create a helper function `createCopyNode(node)`:
   - If the node is already present in the hashmap, return its copy.
   - Otherwise, create a copy of the node and store it in the hashmap.
   - Recursively clone the `next` and `random` nodes.
   - Connect the copied node to the cloned neighbors.
3. Start the cloning process from the head node.
4. Return the cloned head.

# Complexity

- Time complexity:

  $$O(n)$$

  Each node is copied exactly once. All subsequent visits are served from the hashmap.

- Space complexity:

  $$O(n)$$

  - Hashmap stores one copy for each original node.
  - Recursive call stack can grow up to **O(n)** in the worst case.

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
    def __init__(self):
        self.hashmap = {None: None}

    def createCopyNode(self, node):
        if node in self.hashmap:
            return self.hashmap[node]

        copy = Node(node.val)
        self.hashmap[node] = copy

        copy.next = self.createCopyNode(node.next)
        copy.random = self.createCopyNode(node.random)

        return copy

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return self.createCopyNode(head)