from collections import deque


class Solution:
    def reverseFirstKElements(self, queue, k):
        queue = deque(queue)
        stack = [-1] * k
        i = 0
        # Push k popped elements into stack
        while i < k:
            stack[i] = queue.popleft()
            i += 1

        """
        Enqueue those elements into stack. This will ensure that the popped elements wound be enqueued in reverse order.
        """
        i = k - 1
        while i >= 0:
            queue.append(stack[i])
            i -= 1
        """
        Deque the n-k elements from the queue and enqueue them one by one. This will give the final queue with first k elements reversed.
        """
        for i in range(len(queue) - k):
            queue.append(queue.popleft())

        return queue


print(Solution().reverseFirstKElements([1, 2, 3, 4, 5], 3))
