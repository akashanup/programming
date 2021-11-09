"""
Logic:
1. We will be using two min heaps, one for available chairs and the other for occupied chairs.
2. Every time a new friend arrives, we will see that whether there is/are occupied chairs which can be free now(friend sat/sitting on such chairs has left or is living) then we pop these chairs from occupied chairs heap and push into available chairs heap.
3. The we pop the minimum number chair from available chairs heap and assign it to the current arrived friend and push it to occupied chairs heap.
4. When the target friend arrives, we assign the applicable chair and return its number.
"""

import heapq


class Solution:
    def smallestChair(self, times, targetFriend):
        friendsCount = len(times)
        targetFriendTime = times[targetFriend]
        times.sort(key=lambda x: x[0])
        chairs = list(range(friendsCount))
        heapq.heapify(chairs)
        # occupiedChairs will have values like this: [time till it is occupied, chair number]
        occupiedChairs = []
        heapq.heapify(occupiedChairs)
        for arrival, leaving in times:
            while occupiedChairs and occupiedChairs[0][0] <= arrival:
                _, chairAvailable = heapq.heappop(occupiedChairs)
                heapq.heappush(chairs, chairAvailable)
            smallestChairNumberAvailable = heapq.heappop(chairs)
            if arrival == targetFriendTime[0] and leaving == targetFriendTime[1]:
                return smallestChairNumberAvailable
            else:
                heapq.heappush(occupiedChairs, (leaving, smallestChairNumberAvailable))
