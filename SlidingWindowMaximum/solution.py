from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        # Monotonic decreasing queue
        queue = deque()
        maxWindow = []
        for key, num in enumerate(nums):
            # Maintain monotonic decreasing queue.
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(key)
            # Remove first element if it is outside window.
            if queue[0] == key - k:
                queue.popleft()
            # If window has k elements then add to result (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
            if key >= k-1:
                maxWindow.append(nums[queue[0]])
        return maxWindow
