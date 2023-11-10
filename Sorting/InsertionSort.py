"""
Time Complexity: O(N^2)
Space Complexity: O(1)
Stable: Yes
In place: Yes
"""


class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def sortArray(self):
        for i in range(1, len(self.arr)):
            # Current element to be compared
            key = self.arr[i]
            # Move elements of arr[0...i-1], that are greater than key, to one position ahead of their current position
            j = i-1
            while j >= 0 and key < self.arr[j]:
                self.arr[j+1] = self.arr[j]
                j -= 1
            # Insert the key in its correct position
            self.arr[j+1] = key
        return self.arr


array = [5, 4, 2, 3, 1, 1, 5, 4, 2, 3]
print(InsertionSort(array).sortArray())
