"""
Time Complexity: O(N^2)
Space Complexity: O(1)
Stable: Yes
In place: Yes
"""


class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sortArray(self):
        n = len(self.arr)
        for i in range(n-1):
            # Last i elements are already sorted, so we don't need to check them.
            for j in range(n-i-1):
                # Swap if current element is greater than next element.
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        return self.arr


array = [5, 4, 2, 3, 1, 1, 5, 4, 2, 3]
print(BubbleSort(array).sortArray())
