"""
This solution is deletion optimised.
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.frontStack = []
        self.backStack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.frontStack:
            self.backStack.append(self.frontStack.pop())
        self.frontStack.append(x)
        while self.backStack:
            self.frontStack.append(self.backStack.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.frontStack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.frontStack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.frontStack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
