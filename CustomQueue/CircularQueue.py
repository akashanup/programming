from BasicQueue import BasicQueue


class CircularQueue(BasicQueue):
    def __init__(self, size):
        super().__init__(size)

    def enqueue(self, num) -> bool:
        if self.isFull():
            return False
        self.r = (self.r + 1) % self.size
        self.queue[self.r] = num
        self.queueSize += 1
        return True

    def dequeue(self) -> int:
        if self.isEmpty():
            return -1
        self.f = (self.f + 1) % self.size
        self.queueSize -= 1
        return self.queue[self.f]

    def front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.f + 1) % self.size]
