class SeatManager:

    def __init__(self, n: int):
        self.seats = [_ for _ in range(n)]
        heapq.heapify(self.seats)

    def reserve(self) -> int:
        availableSeatNumber = heapq.heappop(self.seats)
        return availableSeatNumber+1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber-1)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)