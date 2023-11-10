"""
Time Complexity: O(N*LogN)
Space Complexity: O(1) NOTE: call stack is ignored.
Stable: Not in the default implementation
In place: Yes
"""


class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def sortArray(self):
        self.__quickSort(0, len(self.arr)-1)
        return self.arr

    def __quickSort(self, start, end):
        if start < end:
            partition = self.__partition(start, end)
            self.__quickSort(start, partition-1)
            self.__quickSort(partition+1, end)

    def __partition(self, start, end):
        pivotIdx = start
        pivot = self.arr[pivotIdx]
        while start < end:
            # Increment start index while the element is less than or equal to the pivot
            while start < len(self.arr) and self.arr[start] <= pivot:
                start += 1
            # Decrement right index while the element is greater than the pivot
            while self.arr[end] > pivot:
                end -= 1
            """
            Swap the elements at start and end as start is now pointing to element greater than pivot and end is 
            now pointing to element less than or equal to pivot.
            """
            if start < end:
                self.arr[start], self.arr[end] = self.arr[end], self.arr[start]
        """
        As we got pivot element index is end, now pivot element is at it's sorted position.
        Return pivot element index i.e,
        """
        self.arr[end], self.arr[pivotIdx] = self.arr[pivotIdx], self.arr[end]
        return end


array = [5, 4, 2, 3, 1, 1, 5, 4, 2, 3]
print(QuickSort(array).sortArray())
