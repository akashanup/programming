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
