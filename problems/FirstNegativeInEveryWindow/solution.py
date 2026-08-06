from collections import deque
from math import ceil


class Solution:
    def firstNegative(self, nums, k):
        # Queue will track the negative elements for all K windows
        queue = deque()
        result = [None] * (len(nums) - k + 1)
        # Find the negative numbers in the original order for the first k-size window
        for i in range(k):
            if nums[i] < 0:
                queue.append(i)

        result[0] = nums[queue[0]] if queue else 0
        r = 1
        # Find all next k-size windows, discard the negative numbers which are outside of k windows and add new negative numbers.
        for i in range(k, len(nums)):
            while queue and i-queue[0] >= k:
                queue.popleft()
            if nums[i] < 0:
                queue.append(i)
            result[r] = nums[queue[0]] if queue else 0
            r += 1

        return result


print(Solution().firstNegative([5, -3, 2, 3, -4], 2))
print(Solution().firstNegative([5, -3, 2, 3, -4], 3))
