class StockPrice:

    def __init__(self):
        self.stocks = {}
        self.currentTimestamp = 0
        self.maximumPrice = []
        self.minimumPrice = []


    def update(self, timestamp: int, price: int) -> None:
        # Update price of the stock at timestamp
        self.stocks[timestamp] = price

        # Update currentTimestamp
        self.currentTimestamp = max(self.currentTimestamp, timestamp)

        # Update maximumPrice heap
        heapq.heappush(self.maximumPrice, [-price, timestamp])

        # Update minimumPrice heap
        heapq.heappush(self.minimumPrice, [price, timestamp])


    def current(self) -> int:
        return self.stocks[self.currentTimestamp]


    def maximum(self) -> int:
        # If the price from the maximumPrice doesn't match the price the stocks for that timestamp then it means the price for that timestamp has been updated. So pop from maximumPrice till we find a matching price.
        maxPrice, timestamp = heapq.heappop(self.maximumPrice)
        while -maxPrice != self.stocks[timestamp]:
            maxPrice, timestamp = heapq.heappop(self.maximumPrice)

        heapq.heappush(self.maximumPrice, [maxPrice, timestamp])
        return -maxPrice


    def minimum(self) -> int:
        # If the price from the minimumPrice doesn't match the price the stocks for that timestamp then it means the price for that timestamp has been updated. So pop from minimumPrice till we find a matching price.
        minPrice, timestamp = heapq.heappop(self.minimumPrice)
        while minPrice != self.stocks[timestamp]:
            minPrice, timestamp = heapq.heappop(self.minimumPrice)

        heapq.heappush(self.minimumPrice, [minPrice, timestamp])
        return minPrice


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
