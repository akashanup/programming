class MinStack:
    def __init__(self, size):
        self.size = size
        self.stack = [[-1, -1] for _ in range(self.size)]
        # Pointer tells the last pushed item
        self.i = -1

    def push(self, num) -> bool:
        if self.isFull():
            return False
        self.i += 1
        if self.i == 0:
            self.stack[self.i] = [num, num]
        else:
            self.stack[self.i] = [num, min(num, self.stack[self.i-1][1])]
        return True

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        popped = self.stack[self.i]
        self.i -= 1
        return popped[0]

    def isFull(self) -> bool:
        return self.i == self.size-1

    def isEmpty(self) -> bool:
        return self.i == -1

    def getTop(self) -> int:
        if self.isEmpty():
            return -1
        return self.stack[self.i][0]

    def getMin(self) -> int:
        if self.isEmpty():
            return -1
        return self.stack[self.i][1]
