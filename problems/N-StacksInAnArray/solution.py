class Solution:
    def __init__(self, n, s):
        # List to store an element
        self.arr = [None] * n
        # List to determine the index of top element of all stacks
        self.top = [-1] * s
        """
        List to determine- 
        the index of next element after stack top
        OR
        the index of next free slot
        """
        self.next = [_ + 1 for _ in range(n)]
        self.next[-1] = -1
        # Variable determines the next free slot to store in arr.
        self.freeSlot = 0

    # Pushes 'X' into the Mth stack. Returns true if it gets pushed into the stack, and false otherwise.
    def push(self, x, m):
        if self.isFull():
            return False
        indexToAdd = self.freeSlot
        self.freeSlot = self.next[self.freeSlot]
        self.arr[indexToAdd] = x
        # This would help while popping.
        self.next[indexToAdd] = self.top[m]
        self.top[m] = indexToAdd
        return True

    # Pops the top element from Mth Stack. Returns -1 if the stack is empty, otherwise returns the popped element.
    def pop(self, m):
        if self.isStackEmpty(m):
            return -1
        topIndex = self.top[m]
        # Update the top with the index of top of mth Stack
        self.top[m] = self.next[topIndex]
        # Update the index of next free slot
        self.next[topIndex] = self.freeSlot
        self.freeSlot = topIndex
        return self.arr[topIndex]

    def isStackEmpty(self, sn):
        return self.top[sn] == -1

    def isFull(self):
        return self.freeSlot == -1


solution = Solution(6, 3)
print(solution.push(10, 1))
print(solution.push(20, 1))
print(solution.push(30, 2))
print(solution.pop(1))
print(solution.pop(1))
print(solution.pop(1))
print(solution.pop(2))
print(solution.pop(2))
