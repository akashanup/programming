class MyStack:

    def __init__(self):
        self.mainQueue = deque()
        self.helperQueue = deque()
        self.topElement = None

    # O(1)
    def push(self, x: int) -> None:
        self.mainQueue.append(x)
        self.topElement = x

    # O(n)
    def pop(self) -> int:
        while len(self.mainQueue) > 1:
            self.topElement = self.mainQueue.popleft()
            self.helperQueue.append(self.topElement)
        topElement = self.mainQueue.popleft()
        self.mainQueue, self.helperQueue = self.helperQueue, self.mainQueue
        return topElement

    # O(1)
    def top(self) -> int:
        return self.topElement

    def empty(self) -> bool:
        return len(self.mainQueue) == 0


# Your MyStack object will be instantiated, and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
