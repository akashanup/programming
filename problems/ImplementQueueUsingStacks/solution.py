"""
This solution is insertion optimised.
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mainStack = []
        self.helperStack = []
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.mainStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from the front of queue and returns that element.
        """
        while len(self.mainStack) > 1:
            self.helperStack.append(self.mainStack.pop())
        popped = self.mainStack.pop()
        while self.helperStack:
            self.mainStack.append(self.helperStack.pop())
        return popped

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.mainStack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.mainStack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
