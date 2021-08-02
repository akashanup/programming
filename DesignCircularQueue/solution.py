class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # Enqueued first item
        if self.head == self.tail == -1:
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.head] = None
        # Dequeued last item
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.k
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.head == self.tail == -1

    def isFull(self) -> bool:
        return self.head == ((self.tail + 1) % self.k)


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print([obj.enQueue(1), obj.enQueue(2), obj.enQueue(3), obj.enQueue(4), obj.Rear(), obj.isFull(), obj.deQueue(), obj.enQueue(4), obj.Rear()])
