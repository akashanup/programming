# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Count number of nodes.
        tempHead = head
        linkedListLength = 0
        while tempHead:
            linkedListLength += 1
            tempHead = tempHead.next
            
        minLengthOfEachPart = linkedListLength // k
        remaining = linkedListLength % k
        
        output = [minLengthOfEachPart for _ in range(k)]
        i = 0
        
        while i < remaining:
            output[i] += 1
            i += 1

        for i in range(k):
            if head:
                nodeCount = 0
                maxNodes = output[i]
                output[i] = head
                while head and nodeCount < maxNodes:
                    currentHead = head
                    head = head.next
                    nodeCount += 1
                currentHead.next = None
            else:
                output[i] = None

        return output
