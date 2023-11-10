"""
Time Complexity: O(N^2)
Space Complexity: O(1)
Stable: No
In place: Yes
"""


class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def sortArray(self):
        n = len(self.arr)
        for i in range(n-1):
            # Assume the value at current index is the minimum
            minValIdx = i
            for j in range(i+1, n):
                if self.arr[j] < self.arr[minValIdx]:
                    minValIdx = j
            # Swap the found min value with the first element in the unsorted part
            self.arr[i], self.arr[minValIdx] = self.arr[minValIdx], self.arr[i]
        return self.arr


array = [5, 4, 2, 3, 1, 1, 5, 4, 2, 3]
print(SelectionSort(array).sortArray())
