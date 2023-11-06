class KQueues:
    def __init__(self, N, Q):
        # List to store an element
        self.arr = [None] * N
        # List to determine the index of front element of all queues
        self.front = [-1] * Q
        # List to determine the index of rear element of all queues
        self.rear = [-1] * Q
        """
        List to determine- 
        the index of previous element before queue's rear
        OR
        the index of next free slot
        """
        self.next = [_+1 for _ in range(N)]
        self.next[-1] = -1
        # Variable determines the next free slot to store in arr.
        self.freeSlot = 0

    def push(self, x, qn):
        if self.isFull():
            return False
        q = qn-1
        indexToAdd = self.freeSlot
        self.freeSlot = self.next[self.freeSlot]
        # If the element x to insert is the first element in q.
        if self.isEmpty(q):
            self.front[q] = indexToAdd
        else:
            # Link the element x with the previous element in q.
            self.next[self.rear[q]] = indexToAdd
        # Update next
        self.next[indexToAdd] = -1
        # Update rear
        self.rear[q] = indexToAdd
        self.arr[indexToAdd] = x
        return True

    def pop(self, qn):
        q = qn-1
        if self.isEmpty(q):
            return -1
        # Element is removed in queue from the front
        indexToRemove = self.front[q]
        self.front[q] = self.next[indexToRemove]
        self.next[indexToRemove] = self.freeSlot
        self.freeSlot = indexToRemove
        return self.arr[indexToRemove]

    def isFull(self):
        return self.freeSlot == -1

    def isEmpty(self, q):
        return self.front[q] == -1


q = KQueues(5, 2)
print(q.push(2, 1))
print(q.push(3, 2))
print(q.push(4, 1))
print(q.push(5, 1))
print(q.pop(2))
print(q.pop(1))
print(q.pop(1))
print(q.pop(1))
print(q.pop(1))
