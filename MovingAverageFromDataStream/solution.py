class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1
        self.items = 0
        self.sum = 0
    
    def isEmpty(self):
        return self.head == self.tail == -1
    
    def isFull(self):
        return self.head == ((self.tail + 1) % self.size)
    
    def enqueue(self, val):
        if self.isFull():
            self.dequeue()
        if self.isEmpty():
            self.head += 1
            self.tail += 1
        else:
            self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = val
        self.sum += val
        self.items += 1

    def dequeue(self):
        if self.isEmpty():
            return
        self.sum -= self.queue[self.head]
        self.items -= 1
        self.queue[self.head] = None
        # Dequeued the only element in queue
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        
    def next(self, val: int) -> float:
        self.enqueue(val)
        return self.sum / self.items


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
