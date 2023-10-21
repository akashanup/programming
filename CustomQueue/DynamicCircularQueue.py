from CircularQueue import CircularQueue


class DynamicCircularQueue(CircularQueue):
    def __init__(self, size):
        super().__init__(size)

    def enqueue(self, num) -> bool:
        if self.isFull():
            temp = [-1]*(len(self.queue)*2)
            for i in range(len(self.queue)):
                temp[i] = self.queue[(self.f+i) % self.size]
            self.f = 0
            self.r = len(self.queue)
            self.queue = temp
            self.size = len(self.queue)
        return super().enqueue(num)
