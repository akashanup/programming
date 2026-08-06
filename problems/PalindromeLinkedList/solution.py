"""
# Intuition

A palindrome reads the same from left to right and right to left. For a linked list, we cannot traverse backwards, so the idea is to split the list into two halves and compare them in opposite directions.

Using the slow and fast pointer technique:

- For an odd-length list, `slow` ends at the middle node.
- For an even-length list, `slow` ends at the first node of the second half.

Instead of reversing the second half, we reverse all nodes before `slow` and then compare the reversed first half with the second half. For odd-length lists, we skip the middle node since it does not affect the palindrome property.

# Approach

1. Use `slow` and `fast` pointers to locate the middle of the list.
2. Determine the start of the second half:
   - If the list length is odd (`fast != None`), skip the middle node by setting `secondHalf = slow.next`.
   - Otherwise, set `secondHalf = slow`.
3. Reverse all nodes before `slow` using a sentinel (dummy) node and head-insertion technique.
4. Compare the reversed first half with the second half node by node.
5. If all values match and both halves are exhausted simultaneously, the list is a palindrome.

# Complexity

- Time complexity:
  
  $$O(n)$$
  
  - Finding the middle takes $$O(n)$$.
  - Reversing the first half takes $$O(n/2)$$.
  - Comparing both halves takes $$O(n/2)$$.

- Space complexity:
  
  $$O(1)$$
  
  Only a few pointers and one dummy node are used.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            # Odd length:
            # slow is at the middle node.
            secondHalf = slow.next
        else:
            # Even length:
            # slow is the first node of the second half.
            secondHalf = slow

        # Reverse all nodes before slow.
        sentinel = ListNode()
        curr = head

        while curr is not slow:
            nextNode = curr.next
            curr.next = sentinel.next
            sentinel.next = curr
            curr = nextNode

        firstHalfReversed = sentinel.next

        while firstHalfReversed and secondHalf:
            if firstHalfReversed.val != secondHalf.val:
                return False

            firstHalfReversed = firstHalfReversed.next
            secondHalf = secondHalf.next

        return not firstHalfReversed and not secondHalf