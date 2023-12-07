import heapq


class Solution:
    def findPlatform(self, arr, dep):
        trains = [[arr[i], dep[i]] for i in range(len(arr))]
        trains.sort()
        heap = []
        heapq.heapify(heap)
        _, departure = trains[0]
        heapq.heappush(heap, departure)
        platforms = 1
        for i in range(1, len(trains)):
            earliestDeparture = heap[0]
            arrival, departure = trains[i]
            if earliestDeparture < arrival:
                heapq.heappop(heap)
            else:
                platforms += 1
            heapq.heappush(heap, departure)
        return platforms


arrival = ["09:00", "09:40", "09:50", "11:00", "15:00", "18:00"]
departure = ["09:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
print(Solution().findPlatform(arrival, departure)) #3
arrival = ["09:00", "09:40"]
departure = ["09:10", "12:00"]
print(Solution().findPlatform(arrival, departure)) #1
