"""
# Intuition

The `next` pointers already form a normal linked list, so we can first create a copy of the entire list without worrying about the `random` pointers.

While creating the copied list, we store a mapping between each original node and its corresponding copied node in a hashmap.

Once all nodes have been copied, every node that a `random` pointer can reference already exists in the hashmap. We can then make a second pass through the hashmap and update the `random` pointers of the copied nodes using the stored mapping.

# Approach

1. Handle the edge case where the list is empty.
2. Create a deep copy of the linked list using only the `next` pointers.
3. While creating the copied list, store the mapping:
   - `original node -> copied node`
4. Iterate through all original nodes stored in the hashmap.
5. For each node, if it has a `random` pointer:
   - Set the copied node's `random` pointer to the copied version of the referenced node using the hashmap.
6. Return the head of the copied list.

# Complexity

- Time complexity:
  
  $$O(n)$$

  - First pass to create all copied nodes: **O(n)**
  - Second pass to update random pointers: **O(n)**

- Space complexity:
  
  $$O(n)$$

  - Hashmap stores one mapping for each node.
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
        
        # Copy linked list without random pointer and save the
        # original node with its corresponding copied node in hashmap.
        hashmap = {}

        copiedList = Node(head.val)
        hashmap[head] = copiedList

        node = copiedList

        while head.next:
            head = head.next

            node.next = Node(head.val)
            node = node.next

            hashmap[head] = node
        
        # Update random pointers of copied nodes.
        for node, copiedNode in hashmap.items():
            if node.random:
                copiedNode.random = hashmap[node.random]
        
        return copiedList
