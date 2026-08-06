"""
# Intuition
Since the digits are stored in reverse order, we can simulate the same process as elementary addition from right to left. Traverse both linked lists simultaneously, add the corresponding digits along with any carry from the previous step, and create a new node containing the current digit of the result. Continue until both lists are exhausted and there is no carry left.


# Approach
1. Create a sentinel (dummy) node to simplify result list construction.
2. Maintain a pointer `curr` to the last node in the result list and a variable `carry`.
3. Iterate while at least one list has remaining nodes or there is a carry.
4. Extract the current digits from both lists; if a list is exhausted, treat its value as `0`.
5. Compute the sum of both digits and the carry.
6. Update the carry using integer division by `10`.
7. Create a new node with the digit `sum % 10` and append it to the result list.
8. Return `sentinel.next`, which points to the head of the resulting linked list.

# Complexity

- Time complexity:
  - $$O(\max(m,n))$$
  - We traverse each linked list at most once.

- Space complexity:
  - $$O(\max(m,n))$$
  - The output linked list stores the result digits.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        curr = sentinel
        carry = 0

        while l1 or l2 or carry:
            x, y = 0, 0

            if l1:
                x = l1.val
                l1 = l1.next

            if l2:
                y = l2.val
                l2 = l2.next

            currVal = x + y + carry
            carry = currVal // 10

            curr.next = ListNode(currVal % 10)
            curr = curr.next

        return sentinel.next