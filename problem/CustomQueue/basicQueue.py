class BasicQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [-1] * self.size
        self.queueSize = 0
        # Pointer tells the last dequeued item
        self.f = -1
        # Pointer tells the last enqueued item
        self.r = -1

    def enqueue(self, num) -> bool:
        if self.isFull():
            return False
        self.r += 1
        self.queue[self.r] = num
        self.queueSize += 1
        return True

    def dequeue(self) -> int:
        if self.isEmpty():
            return -1
        self.f += 1
        self.queueSize -= 1
        return self.queue[self.f]

    def front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.f + 1]

    def rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.r]

    def isEmpty(self) -> bool:
        return self.queueSize == 0

    def isFull(self) -> bool:
        return self.queueSize == self.size
