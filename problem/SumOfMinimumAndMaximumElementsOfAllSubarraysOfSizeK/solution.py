from collections import deque


class Solution:
    def sumOfMaxAndMin(self, arr, k):
        minQueue = deque([])
        maxQueue = deque([])
        minMaxSum = 0

        for i in range(k):
            while minQueue and arr[i] <= arr[minQueue[0]]:
                minQueue.popleft()
            while maxQueue and arr[i] >= arr[maxQueue[0]]:
                maxQueue.popleft()
            minQueue.append(i)
            maxQueue.append(i)
        minMaxSum += arr[minQueue[0]] + arr[maxQueue[0]]

        for i in range(k, len(arr)):
            while minQueue and i - minQueue[0] >= k:
                minQueue.popleft()
            while maxQueue and i - maxQueue[0] >= k:
                maxQueue.popleft()

            while minQueue and arr[i] <= arr[minQueue[0]]:
                minQueue.popleft()
            while maxQueue and arr[i] >= arr[maxQueue[0]]:
                maxQueue.popleft()
            minQueue.append(i)
            maxQueue.append(i)
            minMaxSum += arr[minQueue[0]] + arr[maxQueue[0]]
        return minMaxSum


print(Solution().sumOfMaxAndMin([1, 2, 3, 4, 5], 3))
