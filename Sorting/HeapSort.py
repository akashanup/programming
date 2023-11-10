"""
Time Complexity: O(N*LogN)
Space Complexity: O(1) NOTE: call stack is ignored.
Stable: No
In place: Yes
"""


class HeapSort:
    def __init__(self, arr):
        self.arr = arr

    def sortArray(self):
        self.__heapSort()
        return self.arr

    def __heapSort(self):
        n = len(self.arr)
        # Build max heap
        for i in range((n//2)-1, -1, -1):
            self.__heapify(n, i)
        # Extract element one by one
        for i in range(n-1, -1, -1):
            # Put the max element at the end of unsorted array.
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.__heapify(i, 0)

    def __heapify(self, n, i):
        # Initialize the largest as root
        root = i
        left, right = (2*i)+1, (2*i)+2
        # See if the left child exists and is grater than root
        if left < n and self.arr[left] > self.arr[root]:
            root = left
        # See if the right child exists and is grater than root
        if right < n and self.arr[right] > self.arr[root]:
            root = right
        # Check if root needs to be modified
        if root != i:
            self.arr[root], self.arr[i] = self.arr[i], self.arr[root]
            # Heapify the root
            self.__heapify(n, root)


array = [5, 4, 2, 3, 1, 1, 5, 4, 2, 3]
print(HeapSort(array).sortArray())
