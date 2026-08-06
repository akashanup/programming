from collections import deque


class Solution:
    def interLeaveQueue(self, q):
        queue = deque(q)

        # Dequeue first half of the elements from queue and store in stack(It will be stored in reverse order)
        stack = [None] * (len(q) // 2)
        for i in range(len(stack)):
            stack[i] = queue.popleft()

        # Re enqueue the dequeued elements into queue from stack
        for i in range(len(stack)-1, -1, -1):
            queue.append(stack[i])

        # Swap the first half elements with the second half in the queue
        for i in range(len(q) // 2):
            queue.append(queue.popleft())

        # Dequeue first half of the elements from queue and store in stack (This time it will be in the original order)
        for i in range(len(stack)):
            stack[i] = queue.popleft()

        # Now take one item from stack and another item from queue's from and enqueue them to get the interleaving sequence.
        for i in range(len(stack)-1, -1, -1):
            queue.append(stack[i])
            queue.append(queue.popleft())

        return queue


print(Solution().interLeaveQueue([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(Solution().interLeaveQueue([2, 4, 6, 8, 10, 12]))




