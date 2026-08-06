from minStack import MinStack


class DynamicMinStack(MinStack):
    def __init__(self, size):
        super().__init__(size)

    def push(self, num) -> bool:
        if self.isFull():
            temp = [[-1, -1] for _ in range(len(self.stack)*2)]
            for j in range(self.i+1):
                temp[j] = self.stack[j]
            self.size = len(temp)
            self.stack = temp
        return super().push(num)
