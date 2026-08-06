"""
Logic:
    Sort the trips on the basis of their from location.
    Iterate over the trips and store the passengers of current trip iff If there is enough space for the passengers of current trip.
    Now the question arises as how to determine whether there are enough space or not.
    Solution is, we can use a min heap and store [drop, passengers] in that. Now whenever we find a new trip, we check that whether there is/are any trip(s) whose drop location has arrived or not. If yes then we drop the passengers of those trips to get the space in car.
    After dropping the passengers of previous trips we check that whether there is still enough space for passengers of current trip or not. If yes then we pick those passengers(push into heap) and move to next trip.
"""
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        currentPassengers = 0
        heap = []
        heapq.heapify(heap)
        for (passengers, pickup, drop) in trips:
            # Drop passengers of privous trips whose drop locations might have arrived.
            while heap and heap[0][0] <= pickup:
                trip = heapq.heappop(heap)
                currentPassengers -= trip[1]
            if currentPassengers + passengers <= capacity:
                # Add passengers of current trip
                currentPassengers += passengers
                heapq.heappush(heap, [drop, passengers])
            else:
                return False
        return True
